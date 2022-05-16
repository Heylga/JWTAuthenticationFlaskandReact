import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

export const Signup = () => {
const { store, actions } = useContext(Context);

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
        <div className="col-md-6">
          <label for="inputCity" className="form-label">City</label>
          <input type="text" className="form-control" id="inputCity"/>
        </div>
        <div className="col-md-4">
          <label for="inputState" className="form-label">State</label>
          <select id="inputState" className="form-select">
            <option selected>Choose...</option>
            <option>...</option>
          </select>
        </div>
        <div className="col-md-2">
          <label for="inputZip" className="form-label">Zip</label>
          <input type="text" className="form-control" id="inputZip"/>
        </div>
        <div className="col-12">
          <div className="form-check">
            <input className="form-check-input" type="checkbox" id="gridCheck"/>
            <label className="form-check-label" for="gridCheck">
              Check me out
            </label>
          </div>
        </div>
        <div className="col-12">
          <button type="submit" class="btn btn-primary">Signup</button>
        </div>
      </form>
      </div>
	);
};
