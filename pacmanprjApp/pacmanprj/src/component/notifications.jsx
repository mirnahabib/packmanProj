import React, { useState, useEffect, useRef } from 'react';
import { BiBell } from 'react-icons/bi';




const NotificationsBell = () => {
  const [showNotifications, setShowNotifications] = useState(false);
  const dropdownRef = useRef(null);

  const handleNotificationsClick = () => {
    setShowNotifications(!showNotifications);
  };

 useEffect ( ()=> {

    fetch("api/users/notifications", {
      method: "GET" 
    })
      .then((response) => response.json())
      .then((data)=> console.log(data))
      .catch((error) => console.error(error));
 })


  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setShowNotifications(false);
      }
    };

    document.addEventListener('click', handleClickOutside);

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, [dropdownRef]);

  return (
    <div className="position-relative" ref={dropdownRef}>
      <button
        className="btn btn-link p-0"
        type="button"
        onClick={handleNotificationsClick}
      >
        <BiBell size={24} />
        {showNotifications && (
          <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
            3
            <span className="visually-hidden">unread messages</span>
          </span>
        )}
      </button>
      {showNotifications && (
        <div className="position-absolute top-100 start-50 translate-middle-x">
          <div
            className="bg-light p-3 border"
            style={{ minWidth: '10rem', maxWidth: '20rem' }}
          >
            <h6 className="dropdown-header">Notifications</h6>
            
            <a className="dropdown-item" href="#">
              Notification 1
            </a>
            <a className="dropdown-item" href="#">
              Notification 2
            </a>
            <a className="dropdown-item" href="#">
              Notification 3
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default NotificationsBell;