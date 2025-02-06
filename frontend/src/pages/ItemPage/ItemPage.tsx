import React, { useState } from 'react';
import ItemPageStyles from './ItemPage.module.scss';
import SliderItemPage from "../../components/SliderItemPage/SliderItemPage";

const item = {
    name: 'кофточка базовая черная',
    description: '50% хлопок/50% полиэстер плотность 270 гр.',
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

    const handleSlideChange = (index: number) => {
        setActiveIndex(index); // Обновляем активный слайд
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
                        <SliderItemPage images={item.images} onSlideChange={handleSlideChange} />
                    </div>
                    <div className={ItemPageStyles.items}>
                        {item.images.map((image, index) => (
                            <img
                                key={index}
                                className={`${ItemPageStyles.itemPhoto} ${activeIndex === index ? ItemPageStyles.activeItemPhoto : ''}`}
                                src={image}
                                alt={image}
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
                                    className={ItemPageStyles.sizeItem}
                                    style={{
                                        border: `1px solid ${available ? 'black' : 'gray'}`,
                                        color: available ? 'black' : 'gray'
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
