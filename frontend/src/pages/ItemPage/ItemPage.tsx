import React, { useState } from 'react';
import ItemPageStyles from './ItemPage.module.scss';
import SliderItemPage from "../../components/SliderItemPage/SliderItemPage";

const item = {
    name: 'кофточка базовая черная',
    description: '50% хлопок / 50% полиэстер плотность 270 гр.',
    mainImage: './hudi.svg',
    price: 2500,
    sizes: {
        L: true,
        M: false,
        S: true,
    },
    images: [
        './hudi.svg',
        './cap.svg',
        './fire.svg',
        './tShirt.svg',
        './tShirt.svg',
    ]
};

const ItemPage = () => {
    const [activeIndex, setActiveIndex] = useState(0);
    const [selectedSize, setSelectedSize] = useState<string | null>(null); // Состояние для выбранного размера

    const handleSlideChange = (index: number) => {
        setActiveIndex(index); // Обновляем активный слайд
    };

    const handleSizeClick = (size: string) => {
        setSelectedSize(size); // Обновляем выбранный размер
    };

    return (
        <div className={ItemPageStyles.itemPageWrapper}>
            <div className={ItemPageStyles.navigation}>
                <div className={ItemPageStyles.arrowWrapper}>
                    <img src={'./arrow.svg'} alt={'arrow'} />
                    <p style={{ fontSize: '20px', marginLeft: '8px' }}>Назад</p>
                </div>
                <div><img src={'./close.svg'} alt={'close'} /></div>
            </div>

            <div className={ItemPageStyles.mainWrapper}>
                <div className={ItemPageStyles.left}>
                    <div className={ItemPageStyles.sliderWrapper}>
                        <SliderItemPage images={item.images} activeIndex={activeIndex} onSlideChange={handleSlideChange} />
                    </div>
                    <div className={ItemPageStyles.items}>
                        {item.images.map((image, index) => (
                            <img
                                key={index}
                                onClick={() => handleSlideChange(index)}
                                className={`${ItemPageStyles.itemPhoto} ${activeIndex === index ? ItemPageStyles.activeItemPhoto : ''}`}
                                src={image}
                                alt={image}
                                style={{cursor: 'pointer'}}
                            />
                        ))}
                    </div>
                </div>
                <div className={ItemPageStyles.right}>
                    <div>
                        <p className={ItemPageStyles.nameItem}>{item.name}</p>
                    </div>
                    <div>
                        <p className={ItemPageStyles.priceItem}>{item.price} р.</p>
                    </div>
                    <div>
                        <p className={ItemPageStyles.descriptionItem}>{item.description}</p>
                    </div>
                    <div>
                        <p>Размерчик</p>
                        <div className={ItemPageStyles.sizeList}>
                            {Object.entries(item.sizes).map(([size, available], index) => (
                                <div
                                    key={index}
                                    onClick={() => handleSizeClick(size)} // Обработчик клика для выбора размера
                                    className={ItemPageStyles.sizeItem}
                                    style={{
                                        border: ` ${available && selectedSize === size ? '2px solid black' : '1px solid black'}`, // Бордер 2px для выбранного размера
                                        color: available ? (selectedSize === size ? 'black' : 'black') : 'gray',
                                        cursor: available ? 'pointer' : 'not-allowed', // Курсор для недоступных размеров
                                        padding: '8px', // Добавляем немного отступа для лучшего отображения
                                        margin: '4px', // Отступ между элементами
                                        borderRadius: '4px', // Закругление углов
                                    }}
                                >
                                    {size}
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className={ItemPageStyles.btn}>в корзину</div>
                </div>
            </div>
        </div>
    );
};

export default ItemPage;
