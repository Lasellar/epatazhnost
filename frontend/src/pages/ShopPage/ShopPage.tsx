import React from 'react';
import ShopPageStyles from './ShopPage.module.scss'

const items = [
    {
        src: './hudi.svg',
        name: 'кофточка базовая черная',
        price: 2500,
        description: '50% хлопок/50% полиэстер плотность 270 гр.',
        sizes: {
            L: true,
            M: false,
            S: true,
        }
    },
    {
        src: './tShirt.svg',
        name: 'футболочка базовая черная',
        price: 1800,
        description: '80% хлопок/20% полиэстер плотность 180 гр.',
        sizes: {
            L: true,
            M: true,
            S: false,
        }
    },
    {
        src: './cap.svg',
        name: 'беретик черный',
        price: 3500,
        description: '80% полиэстер/20% нейлон плотность 300 гр.',
        sizes: {
            L: true,
        }

    },
    {
        src: './fire.svg', name: 'жига тупо белая', price: 500, description: 'пластик да алюминий только самовывоз',
        sizes: {
            L: true,
        }
    },
    {
        src: './socks.svg', name: 'носочки белые', price: 400, description: '100% хлопок плотность 260 гр.',
        sizes: {
            L: true,
        }
    },
]

const ItemCard = ({src, name, price, description, sizes}: {
    src: string,
    name: string,
    price: number,
    description: string,
    sizes: { [key: string]: boolean | undefined };
}) => (
    <div className={ShopPageStyles.items}>
        <img src={src} alt={name}/>
        <div className={ShopPageStyles.list}>
            <div>
                <p className={ShopPageStyles.nameItem}>{name}</p>
            </div>
            <div>
                <p className={ShopPageStyles.priceItem}>{price} р.</p>
            </div>
            <div>
                <p className={ShopPageStyles.descriptionItem}>{description}</p>
            </div>
            <div>
                <p>Размерчик</p>
                <div className={ShopPageStyles.sizeList}>
                    {Object.entries(sizes).map(([size, available], index) => (
                        <div
                            key={index}
                            className={ShopPageStyles.sizeItem}
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
        </div>
    </div>
);

const ShopPage = () => {
    return (
        <div className={ShopPageStyles.shopWrapper}>
            <div className={ShopPageStyles.cartWrapper}>
                <img src={'./cart.svg'} alt={'cart'} className={ShopPageStyles.cartItem}/>
            </div>

            <div className={ShopPageStyles.photo}>
                <img src={'./mainPhoto.svg'} alt={'mainPhoto'} className={ShopPageStyles.photoItem}/>
            </div>

            <div className={ShopPageStyles.shopMainWrapper}>
                <nav className={ShopPageStyles.categories}>
                    <p>ВСЕ</p>
                    <p>КОФТОЧКИ</p>
                    <p>ФУТБОЛОЧКИ</p>
                    <p>ШАПОЧКИ</p>
                    <p>МЕЛОЧУШКА</p>
                </nav>

                <div className={ShopPageStyles.itemsWrapper}>
                    {items.map((items, index) => (
                        <ItemCard key={index} {...items}/>
                    ))}
                </div>

            </div>
        </div>
    );
};

export default ShopPage;
