import React from 'react'
import Helmet from "react-helmet";
import Layout from "../../Template/Layout"

import styles from './Home.module.scss'

const Home = () => {
    return (
        // for some reason can't use Fragment for styling
        <div className={`${styles.home_container}`}>
            <Helmet>
                <title>UnEarth</title>
            </Helmet>
            <Layout>
                <main className={styles.top_wrapper}>
                    <div className={styles.inner_top}>
                        THis is where SEarch Form goes
                    </div>
                    
                </main>
                <section className={styles.bottom_wrapper}>
                <div className={styles.inner_bottom}>
                        This is where Form Results will go
                    </div>
                </section>
            </Layout>
        </div>
    )
}

export default Home