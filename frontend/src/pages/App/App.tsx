import React from 'react';
import './App.scss';
import AppHeader from "../../components/AppHeader/AppHeader";
import AppFooter from "../../components/AppFooter/AppFooter";
import ShopPage from "../ShopPage/ShopPage";

function App() {
    return (
        <div>
            <AppHeader/>
            <ShopPage />
            {/*<MainPage/>*/}
            <AppFooter/>
        </div>
    );
}

export default App;
