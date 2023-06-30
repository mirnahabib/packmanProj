import React, { useState, useContext, useEffect } from "react";
import {
  Card,
  Row,
  Col,
  Button,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";
import IconHeart from "./imgs/heart";
import IconHeartFilled from "./imgs/heartfilled";
import { Logos } from "./logos";
import MyUser from "../Contexts/MyUser";

export default function Productcard(props) {
  const [isAddedToWishlist, setIsAddedToWishlist] = useState(204);

  const { isLoggedIn, user } = useContext(MyUser);

  const add2Wishlist = async () => {
    let link = props.product.Link;
    let userID = user.userId;
    fetch("api/favourites/addOrRemove", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId: userID, link: link }),
    })
      .then((response) => {
        setIsAddedToWishlist(response.status);
        return response.json();
      })
      // .then((data) => console.log(data))
      .catch((error) => console.error(error));
  };

  useEffect(() => {
    setIsAddedToWishlist(204);
  }, [props.product]);

  return (
    <Col>
      <Card className="h-100 bg-dark shadow-lg">
        {/* <a
          href={props.product.Link}
          alt={props.product.Title}
          target="_blank"
          rel="noreferrer"
        > */}
        <div
          className="img-props"
          style={{
            height: "300px",
            display: "flex",
            alignItems: "center",
          }}
        >
          {isLoggedIn ? (
            <button
              className={`${isAddedToWishlist === 201 ? "pressed" : ""} fav`}
              onClick={add2Wishlist}
              aria-label="Add to wishlist"
            >
              {isAddedToWishlist === 201 ? <IconHeartFilled /> : <IconHeart />}
            </button>
          ) : (
            ""
          )}

          <img
            className="card-img-top"
            stop
            width="100%"
            src={props.product.Img}
            alt={props.product.Title}
            style={{ objectFit: "contain", maxHeight: "100%" }}
          />
        </div>
        {/* </a> */}
        <Card.Body className="text-light">
          <OverlayTrigger
            placement="bottom"
            overlay={
              props.product.Title.length > 23 ? (
                <Tooltip>{props.product.Title}</Tooltip>
              ) : (
                <></>
              )
            }
          >
            <a
              target="_blank"
              rel="noreferrer"
              href={props.product.Link}
              alt={props.product.Title}
            >
              <Card.Title className="Font product-title-font text-light text-start ">
                {props.product.Title}
              </Card.Title>
            </a>
          </OverlayTrigger>
          {props.product.Price !== 0 ? (
            <Card.Text className="Font product-price-font text-center">
              {props.product.Price} EGP
            </Card.Text>
          ) : (
            <Card.Text className="Font product-price-font text-center">
              Price unavailable
            </Card.Text>
          )}

          <div className="row">
            <div className="col text-center">
              <Button
                className="  Font product-title-font text-light"
                variant="primary"
                href={props.product.Link}
                target="_blank"
              >
                CHECK IT OUT
              </Button>
            </div>

            {
              <div className="d-flex flex-row-reverse">
                <img
                  className=""
                  src={Logos.get(props.product.Shop)}
                  alt={props.product.Shop}
                  height="35em"
                />
              </div>
            }

            {/* <small className="align-self-end text-end shop-name">
                    {props.product.Shop}
                  </small> */}
          </div>
        </Card.Body>
      </Card>
    </Col>
  );
}
