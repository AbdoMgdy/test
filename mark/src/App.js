import React from "react";
// import Form from "./components/form";
import axios from "axios";
import {
  AppBar,
  Tabs,
  Tab,
  Typography,
  Button,
  makeStyles,
} from "@material-ui/core";
import TabPanel from "./components/TabPanel";
import Layout from "./components/Layout";
import Graph from "./components/Graph";
import DropzoneAreaEx from "./components/DraopZoneAreaEx";
import Form from "./components/Form";
function App() {
  const [value, setValue] = React.useState(0);
  const [analyze, setAnalyze] = React.useState(false);
  const [graph, setGraph] = React.useState({ x: [], t: [] });
  const useStyles = makeStyles((theme) => ({
    btn: {
      margin: "2rem auto",
    },
  }));
  const classes = useStyles();
  const changeTab = (event, newValue) => {
    setValue(newValue);
  };
  const handleUpload = (file) => {
    console.log(file);
    const data = new FormData();
    data.append("file", file);
    const url = "http://localhost:5000/upload";
    axios({
      method: "POST",
      url,
      data,
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    })
      .then((res) => {
        console.log(res.data);
        let x = [];
        let t = [];
        res.data.forEach((el) => {
          x.push(el[0]);
          t.push(el[1]);
        });
        setGraph({ x, t });
        setAnalyze(!analyze);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="App">
      <Layout>
        <Typography align="center" variant="h2" gutterBottom>
          Motion Tracking GP 2021
        </Typography>
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
            Analyze
          </Button>
          {/* <CircularProgress size={24} className={classes.buttonProgress} /> */}
        </TabPanel>
        <TabPanel value={value} index={1}>
          <Graph x={graph.x} t={graph.t} />
        </TabPanel>
      </Layout>
    </div>
  );
}

export default App;
