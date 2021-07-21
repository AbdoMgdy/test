import React from "react";
import {
  Box,
  makeStyles,
  Paper,
  useMediaQuery,
  useTheme,
} from "@material-ui/core";
export default function Layout({ children }) {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.down("sm"));
  const useStyles = makeStyles((theme) => ({
    paper: {
      padding: matches ? "0rem" : "2rem",
    },
  }));
  const classes = useStyles();
  return (
    <Box
      width={matches ? "100%" : "70%"}
      mx="auto"
      my={matches ? "0rem" : "4rem"}
    >
      <Paper className={classes.paper}>{children}</Paper>
    </Box>
  );
}
