<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title}}
        </div>

        <!-- Navigation bar -->
        <nav>
            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                <button class="nav-link active" id="nav-stations-tab" data-bs-toggle="tab" data-bs-target="#nav-stations" type="button" role="tab" aria-controls="nav-stations" aria-selected="true">Stations</button>
                <button class="nav-link" id="nav-lines-tab" data-bs-toggle="tab" data-bs-target="#nav-lines" type="button" role="tab" aria-controls="nav-lines" aria-selected="false">Lines</button>
                <button class="nav-link" id="nav-lineStations-tab" data-bs-toggle="tab" data-bs-target="#nav-lineStations" type="button" role="tab" aria-controls="nav-lineStations" aria-selected="false">Line-Stations</button>
            </div>
        </nav>

        <!-- Tab content -->
        <div class="tab-content" id="nav-tabContent">
            <!-- Stations Tab -->
            <div class="tab-pane fade show active" id="nav-stations" role="tabpanel" aria-labelledby="nav-stations-tab">
                <!-- Add Station Modal Button -->
                <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#addStationModal">
                    Add Station
                </button>

                <!-- Station Table -->
                <StationTable
                    :stations="stations"
                    @delete-station="deleteStation"
                    @edit-station="editStation"
                />
            </div>
            <div class="tab-pane fade" id="nav-lines" role="tabpanel" aria-labelledby="nav-lines-tab">
                <!-- Add Line Modal Button -->
                <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#addLineModal">
                    Add Line
                </button>

                <!-- Line Table -->
                <LineTable
                    :lines="lines"
                    @delete-line="deleteLine"
                    @edit-line="editLine"
                />
            </div>
            <div class="tab-pane fade" id="nav-lineStations" role="tabpanel" aria-labelledby="nav-lineStations-tab">
                <!-- Add Line-Station Modal Button -->
                <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#addLineStationModal">
                    Add Line-Station
                </button>

                <!-- Line-Station Table -->
                <LineStationTable
                    :lineStations="lineStations"
                    :lines="lines"
                    :stations="stations"
                    @delete-line-station="deleteLineStation"
                    @edit-line-station="editLineStation"
                />
            </div>
        </div>

        <!-- Add Station Modal -->
        <div class="modal fade" id="addStationModal" tabindex="-1" aria-labelledby="addStationModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addStationModalLabel">Add Station</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newStation.name" type="text" class="form-control" id="name">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createStation" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Line Modal -->
        <div class="modal fade" id="addLineModal" tabindex="-1" aria-labelledby="addLineModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addLineModalLabel">Add Line</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newLine.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Number of Stations</label>
                            <input v-model="newLine.numberOfStations" type="text" class="form-control" id="numberOfStations">
                        </div>
                        <div class="mb-3">
                            <label for="name" class="form-label">Available on Weekends</label>
                            <select v-model="newLine.weekendAvailability" class="form-control" id="weekendAvailability">
                                <option :value="true">Yes</option>
                                <option :value="false">No</option>
                            </select>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createLine" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Line-Station Modal -->
        <div class="modal fade" id="addLineStationModal" tabindex="-1" aria-labelledby="addLineStationModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addLineStationModalLabel">Add Line-Station</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="line" class="form-label">Line</label>
                            <select v-model="newLineStation.line_id" class="form-control" id="line">
                                <option v-for="line in lines" :value="line.id">{{ line.name }}</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="station" class="form-label">Station</label>
                            <select v-model="newLineStation.station_id" class="form-control" id="station">
                                <option v-for="station in stations" :value="station.id">{{ station.name }}</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="order" class="form-label">Position</label>
                            <input v-model="newLineStation.order" type="text" class="form-control" id="order">
                        </div>
                        <div class="mb-3">
                            <label for="notes" class="form-label">Notes</label>
                            <input v-model="newLineStation.notes" type="text" class="form-control" id="notes">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createLineStation" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </template>
  
<script>
    import StationTable from '../components/StationTable.vue'
    import LineTable from '../components/LineTable.vue'
    import LineStationTable from '../components/LineStationTable.vue';

    const baseUrl = 'http://localhost:8000'

    export default {
        components: {
            StationTable,
            LineTable,
            LineStationTable
        },
        data() {
            return {
                title: 'London Tube',
                stations: [],
                newStation: {
                    name: '',
                    lines: []
                },
                lines: [],
                newLine: {
                    name: '',
                    numberOfStations: '',
                    weekendAvailability: '',
                },
                lineStations: [],
                newLineStation: {
                    line_id: '',
                    station_id: '',
                    order: '',
                    notes: ''
                },
            }
        }, 
        async mounted() {
            // const stations_response = await fetch(`${baseUrl}/api/stations`)
            // const stations_data = await stations_response.json()
            // this.stations = stations_data.stations;

            // const lines_response = await fetch(`${baseUrl}/api/lines`)
            // const lines_data = await lines_response.json()
            // this.lines = lines_data.lines;

            // const lineStations_response = await fetch(`${baseUrl}/api/line-stations`)
            // const lineStations_data = await lineStations_response.json()
            // this.lineStations = lineStations_data.lineStations;
            this.stations = await this.fetchData('stations');
            this.lines = await this.fetchData('lines');
            this.lineStations = await this.fetchData('line-stations'); 
        },

        methods: {
            // Fetch data for each type
            async fetchData(type) {
                console.log('fetching data for', type)
                const data = await fetch(`${baseUrl}/api/${type}`);
                const response = await data.json();
                console.log('data: ', response)
                return response ? response[type] : [];
            },
            // Modular fetch request method for all CRUD operations
            async fetchRequest(url, method = 'GET', body = null) {
                const params = { method }
                if (body) {
                    params.headers = { 'Content-Type': 'application/json' }
                    params.body = JSON.stringify(body)
                }
                const response = await fetch(url, params)
                return response.ok ? response.json() : null;
            },
            // Generalized create method
            async createItem(type, collection, newItem) {
                const data = await this.fetchRequest(`${baseUrl}/api/${type}/`, 'POST', newItem);
                if (data) {
                    this[collection].push(data);
                }
            },
            // Generalized edit method
            async editItem(type, collection, item) {
                const response = await this.fetchRequest(`${baseUrl}/api/${type}/${item.id}/`, 'PUT', item);
                if (response) {
                    const index = this[collection].findIndex(i => i.id === item.id);
                    this[collection].splice(index, 1, item);
                }
            },
            // Generalized delete method
            async deleteItem(type, collection, item) {
                if (confirm(`Are you sure you want to delete this ${type.slice(0, -1)}?`)) {
                    const response = await this.fetchRequest(`${baseUrl}/api/${type}/${item.id}/`, 'DELETE');
                    if (response) {
                        this[collection] = this[collection].filter(i => i.id !== item.id);
                    }
                }
            },
            // Specific methods calling generalized methods with the right parameters
            createStation() {
                this.createItem('stations', 'stations', this.newStation);
            },
            createLine() {
                this.createItem('lines', 'lines', this.newLine);
            },
            createLineStation() {
                this.createItem('line-stations', 'lineStations', this.newLineStation);
            },
            editStation(station) {
                this.editItem('station', 'stations', station);
            },
            editLine(line) {
                this.editItem('line', 'lines', line);
            },
            editLineStation(lineStation) {
                this.editItem('line-station', 'lineStations', lineStation);
            },
            deleteStation(station) {
                this.deleteItem('station', 'stations', station);
            },
            deleteLine(line) {
                this.deleteItem('line', 'lines', line);
            },
            deleteLineStation(lineStation) {
                this.deleteItem('line-station', 'lineStations', lineStation);
            }
            // async deleteStation(station) {
            //     if (confirm('Are you sure you want to delete this station?')) {
            //         const response = await fetch(`${baseUrl}/api/station/${station.id}/`, {
            //             method: 'DELETE'
            //         })
            //         if (response.ok) {
            //             this.stations = this.stations.filter(s => s.id !== station.id)
            //         }
            //     }
            // },
            // async deleteLine(line) {
            //     console.log('delete line', line)
            //     if (confirm('Are you sure you want to delete this line?')) {
            //         const response = await fetch(`${baseUrl}/api/line/${line.id}/`, {
            //             method: 'DELETE'
            //         })
            //         if (response.ok) {
            //             this.lines = this.lines.filter(l => l.id !== line.id)
            //         }
            //     }
            // },
            // async createStation() {
            //     console.log(this.newStation)
            //     const response = await fetch(`${baseUrl}/api/stations/`, {
            //         method: 'POST',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(this.newStation)
            //     })
            //     const newStation = await response.json()
            //     this.stations.push(newStation)
            // },
            // async editStation(station) {
            //     const response = await fetch(`${baseUrl}/api/station/${station.id}/`, {
            //         method: 'PUT',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(station)
            //     })
            //     if (response.ok) {
            //         const index = this.stations.findIndex(s => s.id === station.id)
            //         this.stations.splice(index, 1, station)
            //     }
            // },
            // async editLine(line) {
            //     const response = await fetch(`${baseUrl}/api/line/${line.id}/`, {
            //         method: 'PUT',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(line)
            //     })
            //     if (response.ok) {
            //         const index = this.lines.findIndex(l => l.id === line.id)
            //         this.lines.splice(index, 1, line)
            //     }
            // },
            // async createLine() {
            //     const response = await fetch(`${baseUrl}/api/lines/`, {
            //         method: 'POST',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(this.newLine)
            //     })
            //     const newLine = await response.json()
            //     this.lines.push(newLine)
            // },
            // async createLineStation() {
            //     const response = await fetch(`${baseUrl}/api/line-stations/`, {
            //         method: 'POST',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(this.newLineStation)
            //     })
            //     const newLineStation = await response.json()
            //     console.log("new line station: ", newLineStation)
            //     this.lineStations.push(newLineStation)
            // },
            // async editLineStation(lineStation) {
            //     console.log('edit line station', lineStation)
            //     const response = await fetch(`${baseUrl}/api/line-station/${lineStation.id}/`, {
            //         method: 'PUT',
            //         headers: {
            //             'Content-Type': 'application/json'
            //         },
            //         body: JSON.stringify(lineStation)
            //     })
            //     if (response.ok) {
            //         const index = this.lineStations.findIndex(ls => ls.id === lineStation.id)
            //         this.lineStations.splice(index, 1, lineStation)
            //     }
            // },
            // async deleteLineStation(lineStation) {
            //     console.log('delete line station', lineStation)
            //     if (confirm('Are you sure you want to delete this line-station?')) {
            //         const response = await fetch(`${baseUrl}/api/line-station/${lineStation.id}/`, {
            //             method: 'DELETE'
            //         })
            //         if (response.ok) {
            //             this.lineStations = this.lineStations.filter(ls => ls.id !== lineStation.id)
            //         }
            //     }
            // }
        }
    }
</script>
