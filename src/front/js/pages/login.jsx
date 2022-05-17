import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";

export const Login = () => {
const { store, actions } = useContext(Context);
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");
const history = useHistory();
// const token = sessionStorage.getItem("token")


console.log("This is your token", store.token)
const handleClick = () => {
      actions.login(email, password).then(() => {
              history.push("/")
      })
};

if(store.token && store.token != "" && store.token != undefined) history.push("/");

	return (
        <div className="token text-center d-flex justify-content-center">
          {(store.token && store.token!="" && store.token!=undefined) ? "You are logged in with this token" + store.token :
          <div className="form-row m-5">
          <div className="col-md-12">
            <input 
            className="form-control m-2"
            type="text" placeholder="email" value={email} 
            onChange={(e) => setEmail(e.target.value)}/>
          </div>
          <div className="col-md-12">
            <input 
            className="form-control m-2"
            type="password" 
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="col-12">
            <button 
            type="submit" 
            className="btn btn-primary m-3 d-flex justify-content-center"
            onClick={handleClick}
            
            >Log in</button>
          </div>
        </div>
          
          }
        
      </div>
	);
};
