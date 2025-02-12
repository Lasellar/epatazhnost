import React, {useState, useCallback, useRef, CSSProperties, useMemo, useEffect} from 'react';
import SliderStyles from './SliderItemPage.module.scss';
import Modal from "../Modal/Modal";

type SliderProps = {
    images: string[];
    activeIndex: number; // Add activeIndex prop
    onSlideChange?: (index: number) => void;
};

type Position = {
    x: number;
    y: number;
};

const SliderItemPage: React.FC<SliderProps> = ({images, activeIndex, onSlideChange}) => { // Destructure activeIndex
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [currentImageIndex, setCurrentImageIndex] = useState(activeIndex);
    const [isMagnified, setIsMagnified] = useState(false); // Увеличение только для модального окна
    const [position, setPosition] = useState<Position>({x: 0, y: 0}); // Увеличение только для модального окна
    const containerRef = useRef<HTMLDivElement>(null);
    const [transition, setTransition] = useState(false);

    useEffect(() => {
        setCurrentImageIndex(activeIndex); // Update local state when activeIndex changes
    }, [activeIndex]);


    const handleImageClick = (index: number) => {
        setCurrentImageIndex(index);
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
    };

    const nextSlide = useCallback(() => {
        setTransition(true);
        setTimeout(() => {
            setCurrentImageIndex((prevIndex) => {
                const newIndex = (prevIndex + 1) % images.length;
                onSlideChange?.(newIndex); // Notify parent
                return newIndex;
            });
            setTransition(false);
        }, 300);
    }, [images.length, onSlideChange]);

    const prevSlide = useCallback(() => {
        setTransition(true);
        setTimeout(() => {
            setCurrentImageIndex((prevIndex) => {
                const newIndex = (prevIndex - 1 + images.length) % images.length;
                onSlideChange?.(newIndex); // Notify parent
                return newIndex
            });
            setTransition(false);
        }, 300);
    }, [images.length, onSlideChange]);


    const currentImageSrc = images[currentImageIndex];


    const imageStyle = useMemo(() => {
        return {
            width: '530px',
            height: '530px',
            maxWidth: 'unset',
            maxHeight: 'unset',
            transition: 'transform 0.1s linear',
            objectFit: 'cover',
            position: 'absolute',
            top: '50%',
            left: '50%',
            transformOrigin: 'center center',
            transform: 'translate(-50%, -50%)',
            opacity: transition ? 0 : 1,
            transitionProperty: 'opacity',
            transitionDuration: '0.3s',
            transitionTimingFunction: 'ease-in-out',
        } as CSSProperties;
    }, [transition]);

    const imageStyleModal = useMemo(() => {
        return {
            width: '758px',
            height: '758px',
            maxWidth: 'unset',
            maxHeight: 'unset',
            transition: 'transform 0.1s linear',
            objectFit: 'cover',
            position: 'absolute',
            top: '50%',
            left: '50%',
            transformOrigin: 'center center',
            transform: 'translate(-50%, -50%)',
            opacity: transition ? 0 : 1,
            transitionProperty: 'opacity',
            transitionDuration: '0.3s',
            transitionTimingFunction: 'ease-in-out',
        } as CSSProperties;
    }, [transition]);

    // Логика увеличения (только для модального окна)
    const toggleMagnify = () => {
        setIsMagnified((prev) => !prev);
        setPosition({x: 0, y: 0});
    };

    const handleMouseMove = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
        if (!isMagnified || !containerRef.current) return;

        const {clientX, clientY} = e;
        const containerRect = containerRef.current.getBoundingClientRect();

        const {left, top, width, height} = containerRect;

        const x = clientX - left;
        const y = clientY - top;

        const imgWidth = 1200;
        const imgHeight = 1200;

        const maxX = (imgWidth - width) / 2;
        const maxY = (imgHeight - height) / 2;

        const minX = -maxX;

        let newX = (x / width) * (imgWidth - width) - maxX;
        newX = Math.max(Math.min(newX, maxX), minX);

        const newY = Math.min(Math.max((y / height) * (imgHeight - height), -maxY), maxY);

        setPosition({x: -newX, y: -newY});
    }, [isMagnified]);

    return (
        <>

            <div className={SliderStyles.sliderWrapper}>
                <button
                    style={{left: '10px'}}
                    className={SliderStyles.arrowStyle}
                    onClick={(e) => {
                        e.stopPropagation();
                        prevSlide();
                    }}
                >
                    <img src={'./leftArrow.svg'} alt={'leftArrow'}/>
                </button>
                <div
                    className={SliderStyles.containerStyle}
                    ref={containerRef}
                    onClick={() => handleImageClick(currentImageIndex)}
                >
                    <img
                        src={currentImageSrc}
                        alt="fullSize"
                        style={imageStyle}
                    />
                </div>
                <button
                    style={{right: '10px'}}
                    className={SliderStyles.arrowStyle}
                    onClick={(e) => {
                        e.stopPropagation();
                        nextSlide();
                    }}
                >
                    <img src={'./rightArrow.svg'} alt={'rightArrow'}/>
                </button>
            </div>{isModalOpen && (
            <Modal onClose={handleCloseModal}>
                <div className={SliderStyles.sliderWrapper}>
                    <button
                        style={{left: '10px'}}
                        className={SliderStyles.arrowStyleModal}
                        onClick={(e) => {
                            e.stopPropagation();
                            prevSlide();
                        }}
                    >
                        <img src={'./leftArrow.svg'} alt={'leftArrow'}/>
                    </button>
                    <div
                        style={{
                            cursor: isMagnified ? 'zoom-out' : 'zoom-in',
                        }}
                        className={SliderStyles.containerStyleModal}
                        onMouseMove={handleMouseMove}
                        ref={containerRef}
                        onClick={toggleMagnify}
                    >
                        <img
                            src={currentImageSrc}
                            alt="fullSize"
                            style={{
                                ...imageStyleModal,
                                width: isMagnified ? '900px' : '758px',
                                height: isMagnified ? '900px' : '758px',
                                transform: isMagnified
                                    ? `translate(${position.x}px, ${position.y}px) translate(-50%, -50%)`
                                    : 'translate(-50%, -50%)',
                            }}
                        />
                    </div>
                    <button
                        style={{right: '10px'}}
                        className={SliderStyles.arrowStyleModal}
                        onClick={(e) => {
                            e.stopPropagation();
                            nextSlide();
                        }}
                    >
                        <img src={'./rightArrow.svg'} alt={'rightArrow'}/>
                    </button>
                </div>
            </Modal>
        )}
        </>
    );
};

export default SliderItemPage;
