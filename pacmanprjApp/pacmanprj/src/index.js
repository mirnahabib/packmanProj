import React from "react";
import ReactDom from "react-dom";
import App from "./App";
import "./Interceptors/axios";
import MyUserProvider from "./Contexts/MyUserProvider";

ReactDom.render(
  <MyUserProvider>
    <App />
  </MyUserProvider>,
  document.getElementById("root")
);
