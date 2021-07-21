import React from "react";
import axios from "axios";
import {
  AppBar,
  Tabs,
  Tab,
  Typography,
  Button,
  makeStyles,
  CircularProgress,
  Input,
} from "@material-ui/core";
import TabPanel from "./components/TabPanel";
import Layout from "./components/Layout";
import Graph from "./components/Graph";
import DropzoneAreaEx from "./components/DraopZoneAreaEx";
import Form from "./components/Form";
function App() {
  const [value, setValue] = React.useState(0);
  const [mass, setMass] = React.useState(60);
  const [cuttOff, setCuttOff] = React.useState(6);
  const [analyze, setAnalyze] = React.useState(false);
  const [upload, setUpload] = React.useState(false);
  const [graph, setGraph] = React.useState({ x: [], v: [], a: [], t: [] });
  const useStyles = makeStyles((theme) => ({
    btn: {
      margin: "2rem auto",
    },
    select: {
      marginLeft: "2rem",
    },
    input: {
      marginLeft: "2rem",
    },
  }));

  const classes = useStyles();
  const changeTab = (event, newValue) => {
    setValue(newValue);
  };
  const handleUpload = (file) => {
    const data = new FormData();
    data.append("file", file);
    data.append("mass", mass);
    data.append("cutoff", cuttOff);
    const url = "http://127.0.0.1:5000/upload";
    if (file) {
      setUpload(true);
      axios({
        method: "POST",
        url,
        data,
        // headers: {
        //   "Access-Control-Allow-Origin": "*",
        // },
      })
        .then(({ data }) => {
          console.log(data);
          let x = [];
          let v = [];
          let a = [];
          let t = [];
          data.forEach((el) => {
            x.push(el[0]);
            v.push(el[1]);
            a.push(el[2]);
            t.push(el[3]);
          });
          setGraph({ x, v, a, t });
          console.log(x, v, a, t);
          setAnalyze(!analyze);
          setUpload(false);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };

  return (
    <div className="App">
      <Layout>
        <Typography align="center" variant="h2" gutterBottom>
          Motion Tracking GP 2021
        </Typography>
        <Form />
        <AppBar position="static">
          <Tabs value={value} onChange={changeTab}>
            <Tab label="Upload Video" />
            <Tab label="Graph" />
          </Tabs>
        </AppBar>
        <TabPanel value={value} index={0}>
          <DropzoneAreaEx onUpload={handleUpload} />
          <Button
            disabled={!analyze}
            variant="contained"
            color="primary"
            className={classes.btn}
            onClick={() => setValue(1)}
          >
            Show Results
          </Button>
          {/* <Input
            type="number"
            className={classes.input}
            name="mass"
            placeholder="Mass"
            onChange={(event) => setMass(event.target.value)}
          />
          <Input
            type="number"
            className={classes.input}
            name="cutoff"
            placeholder="Cutoff Frequency"
            onChange={(event) => setCuttOff(event.target.value)}
          /> */}
          {upload && (
            <div>
              <h3>Analyzing File</h3>
              <CircularProgress />
            </div>
          )}
          {/* <CircularProgress size={24} className={classes.buttonProgress} /> */}
        </TabPanel>
        <TabPanel value={value} index={1}>
          <Graph x={graph.x} v={graph.v} a={graph.a} t={graph.t} />
        </TabPanel>
      </Layout>
    </div>
  );
}

export default App;
