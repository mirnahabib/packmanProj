import React, { useState, useContext } from "react";
import Chart from "react-apexcharts";
import { Logos } from "./logos";
import { useEffect } from "react";
import { Button } from "react-bootstrap";
import MyUser from "../Contexts/MyUser";

export default function Favcard(props) {
  const [ydata] = useState([]);
  const [graph, setGraph] = useState({
    options: {
      colors: ["#0D6EFD"],
      chart: {
        id: `${props.product.title}`,
      },
      xaxis: {
        categories: [],
        labels: {
          style: {
            colors: "#ffffff",
          },
        },
      },
      yaxis: {
        labels: {
          style: {
            colors: "#ffffff",
          },
        },
      },
    },
    series: [
      {
        name: "",
        data: ydata,
      },
    ],
  });

  useEffect(() => {
    try {
      if (props.price1.prices) {
        props.price1.prices.forEach((product) => {
          const index = product.date.indexOf("T");
          const dateOnly = product.date.slice(0, index);

          ydata.push(product.price);
          setGraph((prevState) => ({
            ...prevState,
            options: {
              xaxis: {
                categories: [
                  ...prevState.options.xaxis.categories,
                  `${dateOnly}`,
                ],
              },
            },
          }));
        });
      }
      ydata.push(props.product.currentPrice);
      setGraph((prevState) => ({
        ...prevState,
        options: {
          xaxis: {
            categories: [
              ...prevState.options.xaxis.categories,
              `${new Date().toISOString().slice(0, 10)}`,
            ],
          },
        },
      }));
    } catch (error) {
      //afks
    }
  }, [props.price1]);

  const { user } = useContext(MyUser);
  const removeItem = async () => {
    let link = props.product.link;
    let userID = user.userId;

    fetch("api/favourites/addOrRemove", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId: userID, link: link }),
    })
      .then((response) => response.json())
      .catch((error) => console.error(error));
    window.location.reload();
  };

  return (
    <div className="row p-3 my-3 border border-warning">
      <div className="col-lg-3 col-12">
        <a href={props.product.link} target="_blank" rel="noreferrer">
          <img
            stop
            width="100%"
            style={{ objectFit: "contain", maxHeight: "100%" }}
            src={props.product.img}
            alt={props.product.title}
          ></img>
        </a>
        <p className="pt-3">
          <img
            className=""
            src={Logos.get(props.product.store)}
            alt={props.product.store}
            height="35em"
          />{" "}
        </p>
      </div>
      <div className="col-lg-6 col-12">
        <a href={props.product.link} target="_blank" rel="noreferrer">
          <p className="text-white">{props.product.title}</p>
        </a>
        <p className="text-white">{props.product.currentPrice} EGP</p>
        <div className="col text-center pt-3">
          <Button
            className="Font product-title-font text-light"
            variant="primary"
            href={props.product.link}
            target="_blank"
          >
            CHECK IT OUT
          </Button>
          <Button
            className="Font product-title-font ms-5 text-light"
            variant="danger"
            onClick={removeItem}
          >
            REMOVE ITEM
          </Button>
        </div>
      </div>
      <div className="col-lg-3 col-12">
        <Chart
          className="text-dark"
          options={graph.options}
          series={graph.series}
          type="area"
          width="100%"
          height="100%"
        />
      </div>
    </div>
  );
}
