import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <ul>
        <li><Link to="/edit">Редагування</Link></li>
        <li><Link to="/survey">Опитування</Link></li>
        <li><Link to="/results">Результати</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
