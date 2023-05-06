import React from "react";
import {
  Card,
  Row,
  Col,
  Button,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";
import IconAmazon from "./imgs/amazon";
import { Logos } from "./logos";

export default function Productcard(props) {
  return (
    <Col>
      <Card className="h-100 bg-dark shadow-lg bor">
        <a
          href={props.product.Link}
          alt={props.product.Title}
          target="_blank"
          rel="noreferrer"
        >
          <div
            className="img-props"
            style={{
              height: "300px",
              display: "flex",
              alignItems: "center",
            }}
          >
            <img
              className="card-img-top"
              stop
              width="100%"
              src={props.product.Img}
              alt={props.product.Title}
              style={{ objectFit: "contain", maxHeight: "100%" }}
            />
          </div>
        </a>
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
              <div class="d-flex flex-row-reverse">
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
