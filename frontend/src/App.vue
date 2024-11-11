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
                    @delete-station="deleteItem('station', 'stations', $event)"
                    @edit-station="editItem('station', 'stations', $event)"
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
                    @delete-line="deleteItem('line', 'lines', $event)"
                    @edit-line="editItem('line', 'lines', $event)"
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
                    @delete-line-station="deleteItem('line-station', 'lineStations', $event)"
                    @edit-line-station="editItem('line-station', 'lineStations', $event)"
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
                        <button type="button" class="btn btn-primary" @click="createItem('stations', 'stations', newStation)" data-bs-dismiss="modal">Save</button>
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
                        <button type="button" class="btn btn-primary" @click="createItem('lines', 'lines', newLine)" data-bs-dismiss="modal">Save</button>
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
                        <button type="button" class="btn btn-primary" @click="createItem('line-stations', 'lineStations', newLineStation)" data-bs-dismiss="modal">Save</button>
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
                return response.ok ? response.json() : {};
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

                    // Refetch lineStations data to capture changes (approach 1 - less lines of code, but requires re-fetching)
                    if (type === 'station' || type === 'line') {
                        this.lineStations = await this.fetchData('line-stations');
                    }
                }
            },
            // Generalized delete method
            async deleteItem(type, collection, item) {
                if (confirm(`Are you sure you want to delete this ${type.slice(0, -1)}?`)) {
                    const response = await this.fetchRequest(`${baseUrl}/api/${type}/${item.id}/`, 'DELETE');
                    if (response) {
                        this[collection] = this[collection].filter(i => i.id !== item.id);

                        // Remove associated lineStations entries without re-fetching (approach 2 - more lines of code, but avoids re-fetching, which is more efficient)
                        if (type === 'station') {
                            console.log('filtering stations')
                            console.log(this.lineStations)
                            this.lineStations = this.lineStations.filter(ls => ls.station.id !== item.id);
                        } else if (type === 'line') {
                            console.log('filtering lines')
                            this.lineStations = this.lineStations.filter(ls => ls.line.id !== item.id);
                        }
                    }
                }
            },
        }
    }
</script>
