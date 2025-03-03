// store.ts
import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import { createWrapper, HYDRATE } from "next-redux-wrapper";
import usersReducer from "./slices/usersSlice";

const makeStore = () =>
  configureStore({
    reducer: {
      users: usersReducer,
    },
  });

export type AppStore = ReturnType<typeof makeStore>;
export type AppState = ReturnType<AppStore["getState"]>;
export type AppDispatch = AppStore["dispatch"];

export const wrapper = createWrapper<AppStore>(makeStore);
