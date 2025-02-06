import React from 'react';
import './App.scss';
import AppHeader from "../../components/AppHeader/AppHeader";
import AppFooter from "../../components/AppFooter/AppFooter";
import ShopPage from "../ShopPage/ShopPage";
import ItemPage from "../ItemPage/ItemPage";
import MainPage from "../MainPage/MainPage";

function App() {
    return (
        <div>
            <AppHeader/>
            <ItemPage />
            {/*<ShopPage />*/}
            {/*<MainPage/>*/}
            <AppFooter/>
        </div>
    );
}

export default App;
