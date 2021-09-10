#!/usr/bin/env python
# coding: utf-8

# #### Spyking circus using spikeinterface
import os
import spikeinterface.extractors as se
import spikeinterface.toolkit as st
import spikeinterface.sorters as ss

# Here are all the informations that we need like the file location
data_path = "P:\\raviku53\\test_recording_file\\"
file_name = "batchrun1.bin"

num_channels = 256  # we need the number of channels only for the .bin file
sampling_frequency = 30000  # in Hz


full_path = data_path + file_name

recording_sparrow = 0
recording_sparrow_filtered = 0

def func():
    print("reading data")

    recording_sparrow = se.BinDatRecordingExtractor(file_path= full_path, sampling_frequency=sampling_frequency, numchan = num_channels, dtype = 'int16')
    
    print("reading probe file")


    Probe = "C:\\Users\\raviku53\\OneDrive - imec\\New Folder\\probeQ2W5.prb"
    recording_sparrow = recording_sparrow.load_probe_file(probe_file=Probe)


    recording_sparrow_filtered = st.preprocessing.bandpass_filter(recording_sparrow, filter_type='butter', freq_min=300, freq_max=6000)
    recording_cmr_sparrow = st.preprocessing.common_reference(recording_sparrow_filtered, reference='median')

    print('Installed sorters', ss.installed_sorters())
    channel_ids = recording_sparrow.get_channel_ids()
    fs = recording_sparrow.get_sampling_frequency()
    num_chan = recording_sparrow.get_num_channels()

    print('Channel ids:', channel_ids)
    print('Sampling frequency:', fs)
    print('Number of channels:', num_chan)

    print(ss.get_default_params('spykingcircus'))

    print("sorting")
    sorting_SC = ss.run_spykingcircus(recording=recording_cmr_sparrow, output_folder = "P:\\raviku53\\test_recording_file\\flask")


    print('Units found by SC:', sorting_SC.get_unit_ids())



    print(sorting_SC)



    print(f'Spike train of a unit: {sorting_SC.get_unit_spike_train(0)}')

    return