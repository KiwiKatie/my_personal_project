import React from 'react';
import router from "./router";
import { RouterProvider } from 'react-router-dom';
// import { ReactDOM } from 'react-dom/client';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
// import Homepage from './components/Homepage.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>

)
