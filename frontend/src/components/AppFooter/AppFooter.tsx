import React from 'react';
import AppFooterStyles from './AppFooter.module.scss'
import MainPageStyles from "../../pages/MainPage/MainPage.module.scss";

const icons = [
    {src: './dscrVk.svg', name: 'dscrVk'},
    {src: './dscrTg.svg', name: 'dscrTg'},
    {src: './dscrYt.svg', name: 'dscrYt'},
]

const IconCard = ({src, name}: { src: string, name: string }) => (
    <div className={AppFooterStyles.icon}>
        <img src={src} alt={name}/>
    </div>
);

const AppFooter = () => {
    return (
        <div className={AppFooterStyles.footerWrapper}>
            <div className={AppFooterStyles.footerContent}>
                <div className={AppFooterStyles.descriptions}>
                    <div className={AppFooterStyles.contacts}>
                        <p className={AppFooterStyles.contactsItem}>Контакты:</p>
                    </div>
                    <div className={AppFooterStyles.address}>
                        <p className={AppFooterStyles.addressItem}>Город Москва, 2025
                            7(964)702-83-10
                            epatazhnost@yandex.ru
                        </p>
                    </div>
                    <div className={AppFooterStyles.social}>
                        <p className={AppFooterStyles.socialItem}>А еще ищи нас в соцсетях:</p>
                        <div className={AppFooterStyles.iconList}>
                            {icons.map((icon, index) => (
                                <IconCard key={index} {...icon}/>
                            ))}
                        </div>
                    </div>
                </div>

                <div className={AppFooterStyles.logo}>
                    <img src="/logoWhite.svg" alt="logoWhite"/>
                </div>
            </div>
        </div>

    );
};

export default AppFooter;
