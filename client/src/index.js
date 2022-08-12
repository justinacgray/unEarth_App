import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import './Static/scss/index.scss'
import {BrowserRouter, Routes, Route} from "react-router-dom";
import App from "./App"
import Home from './Components/Home/Home'
import Dashboard from './Components/Dashboard/Dashboard'
import NavBar from './Template/NavBar/NavBar';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement);

// I could always replace Home component with App.js

root.render(
  <StrictMode>

      <BrowserRouter>
          <Routes>
              <Route path="/" element={<App />} />
              {/* <Route path="/home" element={<Home />} /> */}
              <Route path="/dashboard" element={<Dashboard />}  />
          </Routes>
      </BrowserRouter>
      
    
  </StrictMode>
)
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
