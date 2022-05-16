import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import { useState, useEffect } from "react";

export const Signup = () => {
const { store, actions } = useContext(Context);
const [newUser, setRegistration] = useState();


// useEffect() = {

// }


	return (
        <div>
        <form className="row g-9">
        <div className="col-md-12">
          <label for="inputEmail4" className="form-label">Email</label>
          <input type="email" className="form-control" id="inputEmail4" />
        </div>
        <div claclassNamess="col-md-6">
          <label for="inputPassword4" className="form-label">Password</label>
          <input type="password" className="form-control" id="inputPassword4"/>
        </div>
        <div className="col-12">
          <button 
          type="submit" 
          className="btn btn-primary"
          // onSubmit={}
          
          
          >Signup</button>
        </div>
      </form>
      </div>
	);
};
