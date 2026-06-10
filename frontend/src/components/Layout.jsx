import React from "react";

function Layout({ children }) {
  return (
    <div className="layout">
      <div className="container">
        {children}
      </div>
    </div>
  );
}

export default Layout;
