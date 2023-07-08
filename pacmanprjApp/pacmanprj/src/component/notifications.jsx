import React, { useState, useEffect, useRef, useContext } from "react";
import { BiBell } from "react-icons/bi";
import MyUser from "../Contexts/MyUser";

const NotificationsBell = () => {
  const [showNotifications, setShowNotifications] = useState(false);
  const dropdownRef = useRef(null);
  const [userNots, setUserNots] = useState([]);
  const [unreadNots, setUnreadNots] = useState(0);
  const { isLoggedIn} = useContext(MyUser);

  const handleNotificationsClick = () => {
    setShowNotifications(!showNotifications);
    setUnreadNots(0);
    fetch("api/users/notifications/seen")
      .then((response) => response.json())
      .catch((error) => console.error(error));
  };

  useEffect(() => {
    fetch("api/users/notifications")
      .then((response) => response.json())
      .then((data) => {
        setUserNots(data);
      })
      .catch((error) => console.error(error));
  }, [isLoggedIn]);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setShowNotifications(false);
      }
    };

    document.addEventListener("click", handleClickOutside);

    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  }, [dropdownRef]);

  
  
  useEffect(() => {
    const unseen = userNots.filter((not) => !not.seen).length;
    setUnreadNots(unseen);
  }, [userNots]);
  return (
    <div className="position-relative" ref={dropdownRef}>
      <button
        className="btn btn-link p-0"
        type="button"
        onClick={handleNotificationsClick}
      >
        <BiBell size={24} />
        {(unreadNots !== 0 || showNotifications)  && (
          <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
            {unreadNots}
            <span className="visually-hidden">unread messages</span>
          </span>
        )}
      </button>
      {showNotifications && (
        <div className="position-absolute top-100 start-50 translate-middle-x pt-2">
          <div
            className="bg-dark text-light p-3 border"
            style={{ minWidth: "20rem", maxWidth: "20rem" }}
          >
            <h6 className="dropdown-header border-bottom pb-3">
              Notifications
            </h6>
            {userNots.map((not) =>
              not.seen ? (
                ""
              ) : not.item ? (
                <li
                  title={not.text}
                  className="product-price-font border-bottom"
                >
                  <a href={not.item.link} target="_blank" rel="noopener noreferrer">{not.text.slice(0, 105)}...</a>
                </li>
              ) : (
                <li
                  title={not.text}
                  className="product-price-font border-bottom"
                >
                  {not.text.slice(0, 105)}...
                </li>
              )
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default NotificationsBell;
