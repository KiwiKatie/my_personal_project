import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Homepage from "./components/homepage";
import Signup from "./components/signup";
import Login from "./components/login";
import Creator from "./components/Creator";
import GamePage from "./components/GamePage";

const router = createBrowserRouter([
    {
        path:"/",
        element: <App/>,
        children:[
            {
                index:true,
                element:<Homepage/>
            },
            {
                path:"/login",
                element:<Login/>
            },
            {
                path:"/signup",
                element:<Signup/>
            },
            {
                path:"/creator",
                element:<Creator/>
            },
            {
                path:"/gamepage",
                element:<GamePage/>
            },

        ]
        
    }
]);
export default router