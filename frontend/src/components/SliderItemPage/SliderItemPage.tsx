import React, { useEffect, useRef, useState } from 'react';
import SliderStyles from './SliderItemPage.module.scss';

type SliderProps = {
    images: string[];
    onSlideChange?: (index: number) => void;
};

const SliderItemPage: React.FC<SliderProps> = ({ images, onSlideChange }) => {
    const [activeIndex, setActiveIndex] = useState(0); // Состояние для активного индекса слайда
    const carouselRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (carouselRef.current && onSlideChange) {
            const handleSlide = (event: any) => {
                setActiveIndex(event.to); // Обновляем индекс активного слайда
                onSlideChange(event.to); // Передаем индекс активного слайда
            };

            // Добавляем обработчик события для слайдера
            carouselRef.current.addEventListener('slid.bs.carousel', handleSlide);

            // Убираем обработчик при размонтировании
            return () => {
                carouselRef.current?.removeEventListener('slid.bs.carousel', handleSlide);
            };
        }
    }, [onSlideChange]);

    return (
        <div
            id="carouselExampleIndicators"
            className="carousel slide"
            data-bs-ride="false"
            data-bs-interval="false"
            ref={carouselRef}
        >
            <ol className="carousel-indicators">
                {images.map((_, index) => (
                    <li
                        key={index}
                        data-bs-target="#carouselExampleIndicators"
                        data-bs-slide-to={index}
                        className={index === 0 ? 'active' : ''}
                    ></li>
                ))}
            </ol>

            <div className={`${SliderStyles['carousel-inner']}`}>
                {images.map((image, index) => (
                    <div key={index} className={`carousel-item ${index === 0 ? 'active' : ''}`}>
                        <img
                            src={image}
                            alt={`Slide ${index + 1}`}
                            className={`${SliderStyles['carousel-image']}`}
                        />
                    </div>
                ))}
            </div>

            <button
                className={`carousel-control-prev ${SliderStyles['carousel-control-prev']}`}
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="prev"
                style={{ display: activeIndex === 0 ? 'none' : 'block' }}
            >
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Previous</span>
            </button>
            <button
                className={`carousel-control-next ${SliderStyles['carousel-control-next']}`}
                type="button"
                data-bs-target="#carouselExampleIndicators"
                data-bs-slide="next"
                style={{ display: activeIndex === images.length - 1 ? 'none' : 'block' }}
            >
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Next</span>
            </button>
        </div>
    );
};

export default SliderItemPage;
