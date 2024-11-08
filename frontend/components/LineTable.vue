<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Line</th>
                <th scope="col">Number of Stations</th>
                <th scope="col">Weekend Availability</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(line, index) in lines">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ line.name }}</td>
                <td>
                    <button
                        class="btn btn-sm btn-primary me-2" 
                        data-bs-toggle="modal" 
                        data-bs-target="#editLineModal"
                        @click="selectStation(line)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-line', line)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <!-- Modal -->
    <div class="modal fade" id="editLineModal" tabindex="-1" aria-labelledby="editLineModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="editLineModalLabel">Add Line</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input v-model="updatedLine.name" type="text" class="form-control" id="name">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="$emit('edit-line', updatedLine)" data-bs-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        emits: ['delete-line', 'edit-line'],
        props: {
            lines: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                updatedLine: {
                    id: '',
                    name: '',
                    numberOfStations: '',
                    weekendAvailability: '',
                }
            }
        },
        methods: {
            selectLine(line) {
                this.updatedLine = { ...line }
            },
        }
    }

</script>