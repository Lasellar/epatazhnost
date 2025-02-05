import React from 'react';
import AppHeaderStyles from './AppHeader.module.scss'

const AppHeader = () => {
    return (
        <header>
            <nav className={AppHeaderStyles.nav}>
                <img src="/logo.svg" alt="Логотип"/>
                <div className={AppHeaderStyles.rowColumn}>
                    <p>Магазин</p>
                    <p>Концерты</p>
                    <p>О нас</p>
                    <p>Контакты</p>
                    <img className={AppHeaderStyles.link} src="/vk.svg" alt="Логотип"/>
                    <img className={AppHeaderStyles.link} src="/tg.svg" alt="Логотип"/>
                    <img className={AppHeaderStyles.link} src="/yt.svg" alt="Логотип"/>
                </div>

            </nav>
        </header>
    );
};

export default AppHeader;
