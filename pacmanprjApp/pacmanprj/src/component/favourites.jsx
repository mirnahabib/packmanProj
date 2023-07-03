import React, { useEffect, useState } from "react";
import { Row, Container } from "react-bootstrap";
import Favcard from "./favcard";

export default function Favourites() {
  const [favList, setFavList] = useState([]);
  const [priceList, setPriceList] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        let response = await fetch(`/api/favourites/`);
        const jsonData = await response.json();
        setFavList(jsonData.favlist);
        setPriceList(jsonData.pricesList);
        // console.log(jsonData.pricesList);
        // console.log(jsonData.favlist[0].currentPrice)
      } catch (error) {
        console.error(error);
      }
    })();
  }, []);

  return (
    <div>
      <Container className="text-center Font">
        <Row sm={1} md={1} lg={1}>
          {favList.length !== 0 ? (
            favList.map((product) => {
              const filtered = priceList.find((obj) => obj._id === product._id);
              return <Favcard product={product} price1={filtered} />;
            })
          ) : (
            <h3 className="mt-5 pt-5">Your Favorites will be displayed here</h3>
          )}
        </Row>
      </Container>
    </div>
  );
}
