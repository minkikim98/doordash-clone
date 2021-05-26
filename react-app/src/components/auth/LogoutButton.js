import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
    alert("You have successfully logged out.");
  };

  return <button onClick={onLogout} className="sidebar-menu-option">Logout</button>;
};

export default LogoutButton;
