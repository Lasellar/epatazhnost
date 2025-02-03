import { configureStore } from '@reduxjs/toolkit';

// Пример редьюсера
const counterReducer = (state = { value: 1 }, action: { type: string }) => {
    switch (action.type) {
        case 'increment':
            return { value: state.value + 1 };
        default:
            return state;
    }
};

export const store = configureStore({
    reducer: {
        counter: counterReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
