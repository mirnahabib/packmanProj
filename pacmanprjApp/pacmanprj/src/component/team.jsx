import React from "react";
import { useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import Image from "react-bootstrap/Image";
import omar from "./imgs/omar.jpg";
import telt from "./imgs/telt.jpg";
import "./css/style.css";
import IconGithub from "./imgs/icongithub";

export default function Team() {
  const [Team] = useState([
    {
      Name: "Omar El-Damrany",
      Occupation: "Computer Engineer",
      WorkedOn: "Backend Web Scraping",
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
      Name: "",
      Occupation: "Computer Engineer",
      photo: null,
      WorkedOn: "",
      github: "",
    },
    {
      Name: "",
      Occupation: "Computer Engineer",
      photo: null,
      WorkedOn: "",
      github: "",
    },
    {
      Name: "",
      Occupation: "Computer Engineer",
      photo: null,
      WorkedOn: "",
      github: "",
    },
  ]);

  return (
    <div className="pt-5 text-white">
      <Container className="text-center Font">
        <h1 className="pb-3 mt-3 border-bottom">MEET OUR TEAM</h1>

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
                    <Col sm={12} md={9} lg={9} className="text-center mt-3 mt-lg-5 ">
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
      </Container>
    </div>
  );
}
