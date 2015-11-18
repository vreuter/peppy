# Pipelines

These pipelines use [`pypiper`](https://github.com/epigen/pypiper/) (see the corresponding repository).

# How to use


### Option 1 (clone the repository)

1. Clone this repository.
2. Clone the [`pypiper`](https://github.com/epigen/pypiper/) repository.
3. Produce a config file (it just has a bunch of paths).
4. Go!

```bash
git clone git@github.com:epigen/pipelines.git
git clone git@github.com:epigen/pypiper.git
```

If you are just _using the pypiper pipeline_ in a project, and you are _not developing the pipeline_, you should treat these cloned repos as read-only, frozen code, which should reside in a shared project workspace. There should be only one clone for the project, to avoid running data under changing pipeline versions. In other words, the cloned `pipeline` and `pypiper` repositories *should not change*, and you should not pull any pipeline updates (unless you plan to re-run the whole thing). You could enforce this like so (?):

```bash
chmod -R 544 pypiper
chmod -R 544 pipelines
```

In short, *do not develop pipelines from an active, shared, project-specific clone*. If you want to make changes, consider the following:


### Option 2 (install the packages)

```
pip install https://github.com/epigen/pipelines/zipball/master
pip install https://github.com/epigen/pypiper/zipball/master
```

You will have all runnable pipelines and accessory scripts (from [`scripts/`](scripts/), see below) in your `$PATH`.


# Running pipelines

We use the Looper (`looper.py`) to run pipelines. This just requires a config file passed as an argument, which contains all the settings required. It submits each job to SLURM.

```bash
python ~/repo/pipelines/looper.py -c metadata/config.txt
```

or

```bash
looper -c metadata/config.txt
```

# Config files

Looper requires only one config file. Here's an example:

```yaml
paths:
  output_dir: /fhgfs/groups/lab_bock/shared/projects/example
  pipelines_dir: /fhgfs/groups/lab_bock/shared/projects/example/pipelines
  submission_template: templates/slurm_template.sub

metadata:
  sample_annotation: table_experiments.csv
  merge_table:
  compare_table:

data_sources:
  bsf_samples: "/scratch/lab_bsf/samples/{flowcell}/{flowcell}_{lane}_samples/{flowcell}_{lane}#{BSF_name}.bam"
  encode_rrbs: "/fhgfs/groups/lab_bock/shared/projects/epigenome_compendium/data/encode_rrbs_data_hg19/fastq/{sample_name}.fastq.gz"
```

However, there are more options. See the [project config template](templates/template_pipeline_config.yaml) for a more comprehensive list of options.

We need better documentation on all the options for the config files.


### Data sources

### Pipeline-specific config files

# Post-pipeline processing

Once a pipeline has been run (or is running), you can do some post-processing on the results. Here are some options:

* [scripts/flagCheck.sh](scripts/flagCheck.sh) - Summarize status flag to check on the status (running, completed, or failed) of pipelines.
* [scripts/make_trackhubs.py](scripts/make_trackhubs.py) - Builds a track hub. Just pass it your config file.
* [scripts/summarizePipelineStats.R](scripts/summarizePipelineStats.R) - Run this in the output folder and it will aggregate and summarize all key-value pairs reported in the `PIPE_stats` files, into tables for each pipeline, and a combined table across all pipelines run in this folder.

You can find other examples of stuff in the [scripts/](scripts/) folder.


# Developing pipelines

If you plan to develop pipelines, either by contributing a new pipeline or making changes to an existing pipeline, you should think about things differently. Instead of a project-specific clone, you should just clone the repos to your personal space, where you do the development. Push changes from there. Use this personal repo to run any tests or whatever, but this _is not your final project-specific result_, which should all be run from a frozen clone of the pipeline.


# Accessory scripts

In [`scripts/`](scripts/) there are some small scripts that help with things like monitoring running pipelines, summarizing pipeline outputs, etc. I see this as a folder of __accessory scripts__, not needed by the pipelines. Any scripts used by the pipelines themselves, on the other hand, **should go to** [`pipelines/tools/`](pipelines/tools/).
