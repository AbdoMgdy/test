import React from 'react';
import {Line} from 'react-chartjs-2';
import {Container} from '@material-ui/core'
function Graph({x,t}){
    const state = {
        labels: t,
        datasets: [
            {
                label: x,
                fill: false,
                lineTension: 0.5,
                backgroundColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 2,
                data: x
            }
        ]
    }
    return (
        <Container maxWidth='sm'>
            <Line
            data={state}
            options={{
                title:{
                display:true,
                text:'Displacement with time',
                fontSize:20
                },
                legend:{
                display:false,
                position:'right'
                }
            }}
            />
      </Container>
    );
}
export default Graph;
