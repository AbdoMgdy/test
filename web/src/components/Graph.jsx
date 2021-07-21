import React from "react";
import { Line } from "react-chartjs-2";
import { Container, Select, MenuItem } from "@material-ui/core";
class Graph extends React.Component {
  state = {
    name: "Displacement",
    state: {
      labels: this.props.t,
      datasets: [
        {
          label: this.props.x,
          fill: false,
          lineTension: 0.5,
          backgroundColor: "rgba(75,192,192,1)",
          borderColor: "rgba(0,0,0,1)",
          borderWidth: 2,
          data: this.props.x,
        },
      ],
    },
  };
  handleChange = (e) => {
    if (e.target.value === "x") {
      const x = {
        labels: this.props.t,
        datasets: [
          {
            label: this.props.x,
            fill: false,
            lineTension: 0.5,
            backgroundColor: "rgba(75,192,192,1)",
            borderColor: "rgba(0,0,0,1)",
            borderWidth: 2,
            data: this.props.x,
          },
        ],
      };
      this.setState({ name: "Displacement", state: x });
    } else if (e.target.value === "v") {
      const v = {
        labels: this.props.t,
        datasets: [
          {
            label: this.props.v,
            fill: false,
            lineTension: 0.5,
            backgroundColor: "rgba(75,192,192,1)",
            borderColor: "rgba(0,0,0,1)",
            borderWidth: 2,
            data: this.props.v,
          },
        ],
      };
      this.setState({ name: "Velocity", state: v });
    } else if (e.target.value === "a") {
      const a = {
        labels: this.props.t,
        datasets: [
          {
            label: this.props.a,
            fill: false,
            lineTension: 0.5,
            backgroundColor: "rgba(75,192,192,1)",
            borderColor: "rgba(0,0,0,1)",
            borderWidth: 2,
            data: this.props.a,
          },
        ],
      };
      this.setState({ name: "Acceleration", state: a });
    }
  };
  render() {
    return (
      <Container maxWidth="lg">
        <Select onChange={this.handleChange} value="x">
          <MenuItem value="x">Displacement</MenuItem>
          <MenuItem value="v">Velocity</MenuItem>
          <MenuItem value="a">Acceleration</MenuItem>
        </Select>
        <Line
          data={this.state.state}
          options={{
            title: {
              display: true,
              text: `${this.state.name} with time`,
              fontSize: 20,
            },
            plugins: {
              pan: {
                enabled: true,
              },
              zoom: {
                wheel: {
                  enabled: true,
                },
              },
            },
            legend: {
              display: false,
              position: "right",
            },
          }}
        />
      </Container>
    );
  }
}
export default Graph;
