import React from 'react';
import './App.scss';
import MainPage from "../MainPage/MainPage";
import AppHeader from "../../components/AppHeader/AppHeader";
import AppFooter from "../../components/AppFooter/AppFooter";

function App() {
    return (
        <div>
            <AppHeader/>
            <MainPage/>
            <AppFooter/>
        </div>
    );
}

export default App;
