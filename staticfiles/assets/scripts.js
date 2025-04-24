window.Apex = {
    chart: {
      foreColor: '#ccc',
      toolbar: {
        show: false
      },
    },
    stroke: {
      width: 3
    },
    dataLabels: {
      enabled: false
    },
    tooltip: {
      theme: 'dark'
    },
    grid: {
      borderColor: "#535A6C",
      xaxis: {
        lines: {
          show: true
        }
      }
    }
  };
  
  var spark1 = {
    chart: {
      id: 'spark1',
      group: 'sparks',
      type: 'line',
      height: 80,
      sparkline: {
        enabled: true
      },
      dropShadow: {
        enabled: true,
        top: 1,
        left: 1,
        blur: 2,
        opacity: 0.2,
      }
    },
    series: [{
      data: [95299112.81, 13932241.58]
    }],
    stroke: {
      curve: 'smooth'
    },
    markers: {
      size: 0
    },
    grid: {
      padding: {
        top: 20,
        bottom: 10,
        left: 110
      }
    },
    colors: ['#fff'],
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      x: {
        show: false
      },
      y: {
        title: {
          formatter: function formatter(val) {
            return '';
          }
        }
      }
    }
  }
  
  var spark2 = {
    chart: {
      id: 'spark2',
      group: 'sparks',
      type: 'line',
      height: 80,
      sparkline: {
        enabled: true
      },
      dropShadow: {
        enabled: true,
        top: 1,
        left: 1,
        blur: 2,
        opacity: 0.2,
      }
    },
    series: [{
      data: [64727145.94, 14943540.81]
    }],
    stroke: {
      curve: 'smooth'
    },
    grid: {
      padding: {
        top: 20,
        bottom: 10,
        left: 110
      }
    },
    markers: {
      size: 0
    },
    colors: ['#fff'],
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      x: {
        show: false
      },
      y: {
        title: {
          formatter: function formatter(val) {
            return '';
          }
        }
      }
    }
  }
  
  var spark3 = {
    chart: {
      id: 'spark3',
      group: 'sparks',
      type: 'line',
      height: 80,
      sparkline: {
        enabled: true
      },
      dropShadow: {
        enabled: true,
        top: 1,
        left: 1,
        blur: 2,
        opacity: 0.2,
      }
    },
    series: [{
      data: [39217508.37, 9078818.30]
    }],
    stroke: {
      curve: 'smooth'
    },
    markers: {
      size: 0
    },
    grid: {
      padding: {
        top: 20,
        bottom: 10,
        left: 110
      }
    },
    colors: ['#fff'],
    xaxis: {
      crosshairs: {
        width: 1
      },
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      x: {
        show: false
      },
      y: {
        title: {
          formatter: function formatter(val) {
            return '';
          }
        }
      }
    }
  }
  
  var spark4 = {
    chart: {
      id: 'spark4',
      group: 'sparks',
      type: 'line',
      height: 80,
      sparkline: {
        enabled: true
      },
      dropShadow: {
        enabled: true,
        top: 1,
        left: 1,
        blur: 2,
        opacity: 0.2,
      }
    },
    series: [{
      data: [27582669.97, 3465975.57]
    }],
    stroke: {
      curve: 'smooth'
    },
    markers: {
      size: 0
    },
    grid: {
      padding: {
        top: 20,
        bottom: 10,
        left: 110
      }
    },
    colors: ['#fff'],
    xaxis: {
      crosshairs: {
        width: 1
      },
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      x: {
        show: false
      },
      y: {
        title: {
          formatter: function formatter(val) {
            return '';
          }
        }
      }
    }
  }
  
  new ApexCharts(document.querySelector("#spark1"), spark1).render();
  new ApexCharts(document.querySelector("#spark2"), spark2).render();
  new ApexCharts(document.querySelector("#spark3"), spark3).render();
  new ApexCharts(document.querySelector("#spark4"), spark4).render();
  
// Ventas mensuales por vendedor
// CDMX
  var optionsLine = {
    chart: {
      height: 328,
      type: 'line',
      zoom: {
        enabled: true
      },
      dropShadow: {
        enabled: true,
        top: 3,
        left: 2,
        blur: 4,
        opacity: 1,
      }
    },
    stroke: {
      curve: 'smooth',
      width: 2
    },
    //colors: ["#3F51B5", '#2196F3'],
    series: [{
        name: "Ramon",
        data: [2678025, 1273766.97, 434912]
      },
      {
        name: "Karla",
        data: [950459.50, 317632.70, 239918.50]
      },
      {
        name: "Erick",
        data: [229933, 181037, 194984.50]
      },
      {
        name: "Sandra Nevares",
        data: [442039.70, 507771.61, 154989.50]
      },
      {
        name: "Luis Alejandro",
        data: [525257.90, 383027.50, 91083.00]
      },
      {
        name: "LULU",
        data: [709134.00, 919636.00, 90146.00]
      },
      {
        name: "Carlos Ponce",
        data: [280901.50, 220354.20, 88596.40]
      },
      {
        name: "Jesús",
        data: [263630.20, 21197.00, 66634.50]
      },
      {
        name: "Karina",
        data: [295389.60, 459701.00, 48624.00]
      },
      {
        name: "Rocio",
        data: [409976.00, 372387.50, 44200.50]
      },
      {
        name: "Sofia",
        data: [341176.00, 346410.80, 28621.00]
      },
      {
        name: "Ernesto",
        data: [135365.00, 165280.00, 20042.00]
      }
      
    ],
    title: {
      text: ':',
      align: 'left',
      offsetY: 25,
      offsetX: 20
    },
    subtitle: {
      text: '',
      offsetY: 55,
      offsetX: 20
    },
    markers: {
      size: 6,
      strokeWidth: 0,
      hover: {
        size: 9
      }
    },
    grid: {
      show: true,
      padding: {
        bottom: 0
      }
    },
    labels: ['01/2024', '02/2024', 'Fecha actual'],
    xaxis: {
      tooltip: {
        enabled: true
      }
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
      offsetY: -20
    }
  }
  
  var chartLine = new ApexCharts(document.querySelector('#line-adwords'), optionsLine);
  chartLine.render();

//GUADALAJARA
var optionsLine = {
  chart: {
    height: 328,
    type: 'line',
    zoom: {
      enabled: true
    },
    dropShadow: {
      enabled: true,
      top: 3,
      left: 2,
      blur: 4,
      opacity: 1,
    }
  },
  stroke: {
    curve: 'smooth',
    width: 2
  },
  //colors: ["#3F51B5", '#2196F3'],
  series: [{
      name: "Roberto",
      data: [898608.50, 1120940.20, 3820027.95]
    },
    {
      name: "Rossy",
      data: [613895.10, 608176.90, 255657.01]
    },
    {
      name: "Edith",
      data: [419622.60, 237043.50, 159871.50]
    },
    {
      name: "Rosamaria",
      data: [1250940.60, 994789.70, 131884.10]
    },
    {
      name: "Maria Villegas",
      data: [3005547.10, 849231.60, 52254.40]
    },
    {
      name: "Ale",
      data: [0, 0, 7352]
    },
    {
      name: "Guillermo",
      data: [251853, 264907, 938]
    },
    
  ],
  title: {
    text: ':',
    align: 'left',
    offsetY: 25,
    offsetX: 20
  },
  subtitle: {
    text: '',
    offsetY: 55,
    offsetX: 20
  },
  markers: {
    size: 6,
    strokeWidth: 0,
    hover: {
      size: 9
    }
  },
  grid: {
    show: true,
    padding: {
      bottom: 0
    }
  },
  labels: ['01/2024', '02/2024', 'Fecha actual'],
  xaxis: {
    tooltip: {
      enabled: true
    }
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
      }
    }
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    offsetY: -20
  }
}

var chartLine = new ApexCharts(document.querySelector('#line-adwords-gdl'), optionsLine);
chartLine.render();

//MONTERREY
var optionsLine = {
  chart: {
    height: 328,
    type: 'line',
    zoom: {
      enabled: true
    },
    dropShadow: {
      enabled: true,
      top: 3,
      left: 2,
      blur: 4,
      opacity: 1,
    }
  },
  stroke: {
    curve: 'smooth',
    width: 2
  },
  //colors: ["#3F51B5", '#2196F3'],
  series: [{
      name: "German",
      data: [842956, 1133623, 312857]
    },
    {
      name: "Arline",
      data: [1096176.90, 287475.50, 95535]
    },
    {
      name: "Anahi Martinez",
      data: [2227087, 581620.50, 95391.50]
    },
    {
      name: "Luz",
      data: [391667.80, 1359450, 14297]
    },
    {
      name: "Karla G",
      data: [394274.10, 232180, 14227]
    },
    
  ],
  title: {
    text: ':',
    align: 'left',
    offsetY: 25,
    offsetX: 20
  },
  subtitle: {
    text: '',
    offsetY: 55,
    offsetX: 20
  },
  markers: {
    size: 6,
    strokeWidth: 0,
    hover: {
      size: 9
    }
  },
  grid: {
    show: true,
    padding: {
      bottom: 0
    }
  },
  labels: ['01/2024', '02/2024', 'Fecha actual'],
  xaxis: {
    tooltip: {
      enabled: true
    }
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
      }
    }
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    offsetY: -20
  }
}

var chartLine = new ApexCharts(document.querySelector('#line-adwords-mty'), optionsLine);
chartLine.render();

//LAZZAR
var optionsLine = {
  chart: {
    height: 328,
    type: 'line',
    zoom: {
      enabled: true
    },
    dropShadow: {
      enabled: true,
      top: 3,
      left: 2,
      blur: 4,
      opacity: 1,
    }
  },
  stroke: {
    curve: 'smooth',
    width: 2
  },
  //colors: ["#3F51B5", '#2196F3'],
  series: [{
      name: "Pedidos Online",
      data: [14730, 7685, 7114.50]
    },
    {
      name: "Uniformes-Bordados",
      data: [28566.69, 30553.99, 17818.15]
    },
    {
      name: "Amazon",
      data: [28103, 297096.52, 0]
    },
    {
      name: "Mercado Libre",
      data: [56465.50, 170310.78, 0]
    },
  ],
  title: {
    text: ':',
    align: 'left',
    offsetY: 25,
    offsetX: 20
  },
  subtitle: {
    text: '',
    offsetY: 55,
    offsetX: 20
  },
  markers: {
    size: 6,
    strokeWidth: 0,
    hover: {
      size: 9
    }
  },
  grid: {
    show: true,
    padding: {
      bottom: 0
    }
  },
  labels: ['01/2024', '02/2024', 'Fecha actual'],
  xaxis: {
    tooltip: {
      enabled: true
    }
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
      }
    }
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    offsetY: -20
  }
}

var chartLine = new ApexCharts(document.querySelector('#line-adwords-lzr'), optionsLine);
chartLine.render();

//CHIHUAHUA
var optionsBar = {
  chart: {
    height: 380,
    type: 'bar',
    stacked: true,
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      horizontal: true,
    },
  },
  series: [{
    name: "Maria Alcaraz",
    data: [329689, 527275.90, 64752.50]
  },
  {
    name: "Cristy Alcaraz",
    data: [67355.50, 80115.70, 0]
  }],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  fill: {
    opacity: 1
  },

}

var chartBar = new ApexCharts(
  document.querySelector("#barchart-chi"),
  optionsBar
);

chartBar.render();

// Porcentajes
  var optionsCircle4 = {
    chart: {
      type: 'radialBar',
      height: 350,
      width: 380,
    },
    plotOptions: {
      radialBar: {
        size: undefined,
        inverseOrder: true,
        hollow: {
          margin: 5,
          size: '48%',
          background: 'transparent',
  
        },
        track: {
          show: false,
        },
        startAngle: -180,
        endAngle: 180
  
      },
    },
    stroke: {
      lineCap: 'round'
    },
    series: [17, 32, 7],
    labels: ['2021', '2022', '2023'],
    legend: {
      show: true,
      floating: true,
      position: 'right',
      offsetX: 70,
      offsetY: 240
    },
  }
  
  var chartCircle4 = new ApexCharts(document.querySelector('#radialBarBottom'), optionsCircle4);
  chartCircle4.render();
  

  
// Tijuana
  var optionsArea = {
    chart: {
      height: 380,
      type: 'area',
      stacked: false,
    },
    stroke: {
      curve: 'straight'
    },
    series: [{
        name: "Karem",
        data: [397671, 151464, 25792.50]
      },
      {
        name: "Patsy",
        data: [22793.50, 741599.70, 24661]
      },
      {
        name: "Alexis",
        data: [734160.70, 209911.60, 0]
      }
    ],
    xaxis: {
      categories: ['01/2024', '02/2024', 'Fecha Actual'],
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      followCursor: true
    },
    fill: {
      opacity: 1,
    },
  
  }
  
  var chartArea = new ApexCharts(
    document.querySelector("#areachart-tj"),
    optionsArea
  );
  
  chartArea.render();

  // Queretaro
  var optionsArea = {
    chart: {
      height: 380,
      type: 'area',
      stacked: false,
    },
    stroke: {
      curve: 'straight'
    },
    series: [{
        name: "Gaby Barroso",
        data: [270883, 253168, 226852]
      },
      {
        name: "Alejandro Barroso",
        data: [934077.12, 427481.85, 164338.50]
      },
      {
        name: "Norma Velazquez",
        data: [476977, 704942.10, 7256]
      }
    ],
    xaxis: {
      categories: ['01/2024', '02/2024', 'Fecha Actual'],
    },
    yaxis: {
      labels: {
        formatter: function (value) {
          return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
        }
      }
    },
    tooltip: {
      followCursor: true
    },
    fill: {
      opacity: 1,
    },
  
  }
  
  var chartArea = new ApexCharts(
    document.querySelector("#areachart-Qto"),
    optionsArea
  );
  
  chartArea.render();

// Puebla
var optionsArea = {
  chart: {
    height: 380,
    type: 'area',
    stacked: false,
  },
  stroke: {
    curve: 'straight'
  },
  series: [{
      name: "Juan Pablo",
      data: [413805.50, 588610.50, 147685]
    },
    {
      name: "Emili",
      data: [188638, 6722.50, 21105.20]
    },
  ],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
      }
    }
  },
  tooltip: {
    followCursor: true
  },
  fill: {
    opacity: 1,
  },

}

var chartArea = new ApexCharts(
  document.querySelector("#areachart-Pue"),
  optionsArea
);

chartArea.render();



// San Luis Potosi
var optionsArea = {
  chart: {
    height: 380,
    type: 'area',
    stacked: false,
  },
  stroke: {
    curve: 'straight'
  },
  series: [{
      name: "Hector",
      data: [219215.40, 304910.50, 54955]
    },
    {
      name: "Perla",
      data: [327386.50, 177459.30, 23410.50]
    },
  ],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
      }
    }
  },
  tooltip: {
    followCursor: true
  },
  fill: {
    opacity: 1,
  },

}

var chartArea = new ApexCharts(
  document.querySelector("#areachart-SLP"),
  optionsArea
);

chartArea.render();


// Veracruz
var optionsBar = {
  chart: {
    height: 380,
    type: 'bar',
    stacked: true,
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      horizontal: false,
    },
  },
  series: [{
    name: 'Alicia',
    data: [100068.60, 187800, 36170.00]
  }],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  fill: {
    opacity: 1
  },

}

var chartBar = new ApexCharts(
  document.querySelector("#barchart"),
  optionsBar
);

chartBar.render();

// León
var optionsBar = {
  chart: {
    height: 380,
    type: 'bar',
    stacked: true,
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      horizontal: false,
    },
  },
  series: [{
    name: 'Cristy',
    data: [515692, 1119975, 347418]
  }],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  fill: {
    opacity: 1
  },

}

var chartBar = new ApexCharts(
  document.querySelector("#barchart-leo"),
  optionsBar
);

chartBar.render();

// Culiacan
var optionsBar = {
  chart: {
    height: 380,
    type: 'bar',
    stacked: true,
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      horizontal: true,
    },
  },
  series: [{
    name: 'Marcela',
    data: [179161, 304225.10, 294846]
  }],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  fill: {
    opacity: 1
  },

}

var chartBar = new ApexCharts(
  document.querySelector("#barchart-snl"),
  optionsBar
);

chartBar.render();



// Ixtapa
var optionsBar = {
  chart: {
    height: 380,
    type: 'bar',
    stacked: true,
  },
  plotOptions: {
    bar: {
      columnWidth: '30%',
      horizontal: false,
    },
  },
  series: [{
    name: 'Angelica',
    data: [200506.20, 481753.70, 52612]
  }],
  xaxis: {
    categories: ['01/2024', '02/2024', 'Fecha Actual'],
  },
  fill: {
    opacity: 1
  },

}

var chartBar = new ApexCharts(
  document.querySelector("#barchart-Ixt"),
  optionsBar
);

chartBar.render();