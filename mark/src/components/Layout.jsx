import React from "react";
import { Box, makeStyles, Paper } from "@material-ui/core";
export default function Layout({ children }) {
  const useStyles = makeStyles((theme) => ({
    paper: {
      padding: "2rem",
    },
  }));
  //   const mockData = [
  //     [1.5, 2.5],
  //     [1.8, 3.5],
  //     [2, 4],
  //     [1.5, 2.5],
  //     [1.8, 3.5],
  //     [2, 4],
  //     [1.5, 2.5],
  //     [1.8, 3.5],
  //     [2, 4],
  //   ];
  const classes = useStyles();
  return (
    <Box width="70%" mx="auto" my="4rem">
      <Paper className={classes.paper}>{children}</Paper>
    </Box>
  );
}
