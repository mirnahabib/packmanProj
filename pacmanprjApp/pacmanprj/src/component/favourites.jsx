import React, { useEffect, useState } from "react";
import { Row } from "react-bootstrap";
import Productcard from "./productcard";


export default function Favourites() {
  const [favList, setfavList] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        let response = await fetch(`/api/favourites/`);
        const jsonData = await response.json();
        setfavList(jsonData.favlist);
        console.log(jsonData.favlist);
        console.log(jsonData.favlist[0].currentPrice)
      } catch (error) {
        console.error(error);
      }
    })();
  }, []);

  return (
    <>
      <div className=" row position-absolute top-50 start-50 translate-middle Font align-items-center justify-content-center text-center">
        <div className="row">
          <div className="col-12 ">
            {favList.map((product) => (
              <div className="p-3 my-3 border border-warning">
                <p>{product.title}</p>
                <p>{product.currentPrice} EGP</p>
                <a href={product.link}><img src ={product.img} alt={product.title}></img></a>
                <small>{product.store}</small>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
