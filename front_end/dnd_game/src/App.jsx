import React from 'react';
import {Link, Outlet} from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './index.css';

export default function App() {

  return (
        <>
        {/* <Homepage/> */}
        <Outlet/>
        </>
  );
}


