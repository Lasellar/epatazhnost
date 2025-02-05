import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.scss';
import App from './pages/App/App';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.scss';
import { Provider } from 'react-redux';
import { store } from './store';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <Provider store={store}>
            <App />
        </Provider>
    </React.StrictMode>
);

