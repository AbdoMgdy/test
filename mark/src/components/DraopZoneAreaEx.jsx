import React, { Component } from "react";
import { DropzoneArea } from "material-ui-dropzone";

class DropzoneAreaEx extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
    };
  }
  handleChange(files) {
    // this.setState({
    //   files: files,
    // });
    this.props.onUpload(files[0]);
  }
  render() {
    return <DropzoneArea onChange={this.handleChange.bind(this)} />;
  }
}

export default DropzoneAreaEx;
