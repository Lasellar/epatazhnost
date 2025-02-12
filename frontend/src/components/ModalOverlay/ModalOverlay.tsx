import React from 'react';
import ModalOverlayStyles from './ModalOverlay.module.css';

interface ModalOverlayProps {
    onClose: () => void;
}

const ModalOverlay = ({onClose}: ModalOverlayProps) => {
    return (
        <div className={ModalOverlayStyles.modalOverlay} onClick={onClose} data-cy="modal-close-overlay"></div>
    );
};

export default ModalOverlay;
