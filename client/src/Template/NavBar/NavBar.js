import React from 'react'
import { Link } from "react-router-dom";
import styles from './NavBar.module.scss';
import * as Icons from "react-icons/go"

const NavBar = () => {
  return (
        <nav className={`${styles.nav_container} `}>
          <Link to="/" className={`${styles.logo} font-logo `}> 
              UnEarth
              <Icons.GoGlobe /> 
          </Link>  
          <ul className={styles.nav_items}>
            <li>
                <Link to="#" className={styles.nav_item}>Something</Link>
            </li>
            <li>
                <Link to="#" className={styles.nav_item}>Something</Link>
            </li>
            <li>
                <Link to="#" className={styles.nav_item}>Something</Link>
            </li>
            <li>
                <Link to="#" className={styles.nav_item}>Something</Link>
            </li>
          </ul>
          <Link to="#">
            <button className={styles.sign_up_btn}>Sign Up / Log In</button>
          </Link>
        </nav>
  )
}

export default NavBar