import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Link } from "react-router-dom";
import { Login } from "./login.jsx";

export const Home = () => {
	const { store, actions } = useContext(Context);

	useEffect(() => {
		if (store.token && store.token != "" && store.token != undefined) actions.getMessage();
	}, 
	[store.token]
	);

	// fetch('https://3001-heylga-jwtauthenticatio-1yxluaboq88.ws-eu45.gitpod.io/admin/')
	// .then((promise) => promise.json)
	// .then((response) => console.log('this from own backend', response))

	return (
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<p>
				<img src={rigoImageUrl} />
			</p>
			
			<Link to="/login">
						<button href="#" className="btn btn-outline-primary">
							Click to Log In
						</button>
					</Link>
			<div className="alert alert-info">
				{store.message}
			</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://github.com/4GeeksAcademy/react-flask-hello/tree/95e0540bd1422249c3004f149825285118594325/docs">
					Read documentation
				</a>
			</p>
		</div>
	);
};
