import React from 'react'
import {
    Card,
    Row,
    Col,
    Button,
    OverlayTrigger,
    Tooltip,
  } from "react-bootstrap";
import IconAmazon from "./imgs/amazon";
import twoB from "./imgs/icons/twoB.png";
import bershka from "./imgs/icons/bershka.png";
import branto from "./imgs/icons/branto.png";
import carrefour from "./imgs/icons/carrefour.png";
import dpphone from "./imgs/icons/dpphone.jpg";
import egygamer from "./imgs/icons/egygamer.png";
import faces from "./imgs/icons/faces.png";
import games2egypt from "./imgs/icons/games2egypt.jpg";
import gameworld from "./imgs/icons/gameworld.jpg";
import gourmet from "./imgs/icons/gourmet.jpg";
import handm from "./imgs/icons/handm.png";
import hubfurniture from "./imgs/icons/hubfurniture.png";
import hyper1 from "./imgs/icons/hyper1.jpg";
import ikea from "./imgs/icons/ikea.png";
import jumia from "./imgs/icons/jumia.png";
import lcwaikiki from "./imgs/icons/lcwaikiki.png";
import max from "./imgs/icons/max.png";
import noon from "./imgs/icons/noon.png";
import olx from "./imgs/icons/olx.jpg";
import opensooq from "./imgs/icons/opensooq.png";
import select from "./imgs/icons/select.png";
import shamy from "./imgs/icons/shamy.jpg";
import spinneys from "./imgs/icons/spinneys.png";


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
                {
                  props.product.Price !==0 ? (
                    <Card.Text className="Font product-price-font text-center">
                  {props.product.Price} EGP
                </Card.Text>

                  ) : <Card.Text className="Font product-price-font text-center">
                  Price unavailable
                </Card.Text>
                }
                
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
                  {(props.product.Shop==="Amazon"? <IconAmazon/>:"")  }    
                  {(props.product.Shop==="2B"? <img src={twoB} style={{width:100}} />:"")}
                  {(props.product.Shop==="Bershka"? <img src={bershka}  />:"")}
                  {(props.product.Shop==="Branto"? <img src={branto}  />:"")}
                  {(props.product.Shop==="Carrefour"? <img src={carrefour} />:"")}
                  {(props.product.Shop==="Dubai Phone"? <img src={dpphone} />:"")}
                  {(props.product.Shop==="Egygamer"? <img src={egygamer} />:"")}
                  {(props.product.Shop==="Faces"? <img src={faces} />:"")}
                  {(props.product.Shop==="Games2egypt"? <img src={games2egypt} />:"")}
                  {(props.product.Shop==="Gameworld"? <img src={gameworld} />:"")}
                  {(props.product.Shop==="Gourmet"? <img src={gourmet} />:"")}
                  {(props.product.Shop==="H&M"? <img src={handm} />:"")}
                  {(props.product.Shop==="HubFurniture"? <img src={hubfurniture} />:"")}
                  {(props.product.Shop==="Hyperone"? <img src={hyper1} />:"")}
                  {(props.product.Shop==="Ikea"? <img src={ikea} />:"")}
                  {(props.product.Shop==="Jumia"? <img src={jumia} />:"")}
                  {(props.product.Shop==="LCWaikiki"? <img src={lcwaikiki} />:"")}
                  {(props.product.Shop==="Max"? <img src={max} />:"")}
                  {(props.product.Shop==="Noon"? <img src={noon} />:"")}
                  {(props.product.Shop==="OLX"? <img src={olx} />:"")}
                  {(props.product.Shop==="Opensooq"? <img src={opensooq} />:"")}
                  {(props.product.Shop==="Select"? <img src={select} />:"")}
                  {(props.product.Shop==="Shamy"? <img src={shamy} />:"")}
                  {(props.product.Shop==="Spinneys"? <img src={spinneys} />:"")}
                  
                  
                  {/* <small className="align-self-end text-end shop-name">
                    {props.product.Shop}
                  </small> */}
                </div>
              </Card.Body>
            </Card>
          </Col>
  )
}
