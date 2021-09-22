import React, { Fragment } from "react";

import loader from "./loader1.gif";
const Loader = () => (
  <Fragment>
    <img
      id="manu"
      src={loader}
      alt="Loading..."
      style={{ width: "150px", display: "block", padding:"0% 0% 0% 0%",margin: "20% auto auto auto" }} 
    />
  </Fragment>
);
export default Loader;
