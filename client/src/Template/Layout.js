import NavBar from "./NavBar/NavBar";
import Footer from "./Footer/Footer";


const Layout = (props) => {
    const { children } = props;
    return (
        <div className="">
            <NavBar />
            <main className="">
                {children}
            </main>
            <Footer />
        </div>
    );
};

export default Layout;