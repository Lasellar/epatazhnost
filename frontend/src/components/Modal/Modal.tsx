import React, {useEffect} from 'react';
import ReactDOM from 'react-dom';
import ModalOverlayStyles from './Modal.module.css';
import ModalOverlay from "../ModalOverlay/ModalOverlay";

export interface ModalProps {
    onClose: () => void;
    children: React.ReactNode;
}


const Modal = ({onClose, children}: ModalProps) => {

    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'Escape') {
                onClose();
            }
        };

        const handleClickOutside = (e: MouseEvent) => {
            if ((e.target as HTMLElement).classList.contains(ModalOverlayStyles.modalOverlay)) {
                onClose();
            }
        };

        document.addEventListener('keydown', handleKeyDown);
        document.addEventListener('mousedown', handleClickOutside);

        return () => {
            document.removeEventListener('keydown', handleKeyDown);
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, [onClose]);

    const modalsRoot = document.getElementById('modals');
    if (!modalsRoot) return null;

    return ReactDOM.createPortal(
        <>
            <ModalOverlay onClose={onClose}/>
            <div className={ModalOverlayStyles.modal}>
                <div className={ModalOverlayStyles.modalHeader}>
                    <button className={ModalOverlayStyles.closeBtn} onClick={onClose} data-cy="modal-close">
                        <img src={'./close.svg'} alt={'close'}/>
                    </button>
                </div>
                {children}
            </div>
        </>,
        modalsRoot
    );
};

export default Modal;
