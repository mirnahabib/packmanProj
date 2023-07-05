import React from "react";
import { useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import Image from "react-bootstrap/Image";
import omar from "./imgs/omar.jpg";
import telt from "./imgs/telt.jpg";
import mostafa from "./imgs/mostafa.JPG";
import "./css/style.css";
import IconGithub from "./imgs/icongithub";
import { Stores } from "./logos";

export default function Team() {
  const [Team] = useState([
    {
      Name: "Omar El-Damrany",
      Occupation: "Computer Engineer",
      WorkedOn: "Backend web scraping",
      photo: omar,
      github: "https://github.com/omar-eldamrany",
    },
    {
      Name: "Mahmoud El Telt",
      Occupation: "Computer Engineer",
      photo: telt,
      WorkedOn: "NodeJs/ExpressJS backend",
      github: "https://github.com/ElteltM",
    },
    {
      Name: "Mostafa Mohamed Kamal",
      Occupation: "Computer Engineer",
      photo: mostafa,
      WorkedOn: "Frontend to backend/Authentication",
      github: "https://github.com/Ulsur",
    },
    {
      Name: "Mirna Habib",
      Occupation: "Computer Engineer",
      photo: null,
      WorkedOn: "Frontend",
      github: "https://github.com/mirnahabib",
    },
    {
      Name: "Yasmine Fayed",
      Occupation: "Computer Engineer",
      photo: null,
      WorkedOn: "Frontend and Market Research",
      github: "https://github.com/Yasminefayed",
    },
  ]);

  return (
    <div className="pt-5">
      <Container className="text-center Font text-white">
        <h1 className="pb-3 mt-3 border-bottom">Packman</h1>
        <p className="pb-3 pt-3 ">
          Packman is an online shopping tool that helps people find their
          desired products easily and also find the best deal for these products
          by collecting the same or similar products from different web stores
          depending on your search term.
          <br></br>
          <br></br>
          Packman brings you products from more than 40 websites that are mostly
          inside Egypt, it has a feature that enables you to find used products
          as well!
          <br></br>
          <br></br>
          <i className="text-danger">Disclaimer:</i> Packman does NOT sell any
          products, only fetches products from different websites, we do NOT own
          any products or any of the stores mentioned.
        </p>

        <h1 className="pb-3 mt-3 pt-5 border-bottom">MEET OUR TEAM</h1>

        {Team && (
          <div className="container pt-5">
            <div className="row">
              {Team.map((item) => {
                return (
                  <Row className="pt-5 ">
                    <Col className="flicker-in-1  " sm={12} md={3} lg={3}>
                      <Image
                        className="team-border"
                        src={item.photo}
                        roundedCircle
                        fluid
                      />
                    </Col>
                    <Col
                      sm={12}
                      md={9}
                      lg={9}
                      className="text-center mt-3 mt-lg-5 "
                    >
                      <div className="container heartbeat">
                        <div className="row">
                          <div className="col-12">
                            <h4>{item.Name}</h4>
                          </div>
                        </div>
                        <div className="row pt-3">
                          <div className="col-12 info">
                            <p>
                              <small>{item.Occupation}</small>
                            </p>
                            <p>
                              <small>{item.WorkedOn}</small>
                            </p>
                            <a
                              className="flicker-in-1"
                              target="_blank"
                              href={item.github}
                              rel="noreferrer"
                            >
                              <IconGithub />
                            </a>
                          </div>
                        </div>
                      </div>
                    </Col>
                  </Row>
                );
              })}
            </div>
          </div>
        )}
        <h1 className="pb-3 mt-3 border-bottom text-white pt-5">Stores</h1>

        <Row sm={1} md={3} lg={4} className="g-4">
          {Stores.map((store) => (
            <div>
              <p className="text-white">{store.name}</p>
              <img src={store.picture} alt={store.name} height="60em"></img>
            </div>
          ))}
        </Row>
      </Container>
    </div>
  );
}
