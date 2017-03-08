/*******************************************************************************
 * Copyright 2015-16 AutoCognite Testing Research Pvt Ltd
 * 
 * Website: www.AutoCognite.com
 * Email: support [at] autocognite.com
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/
package com.autocognite.pvt.batteries.databroker;

import java.util.ArrayList;
import java.util.Iterator;

import com.autocognite.arjuna.interfaces.DataRecord;
import com.autocognite.pvt.batteries.enums.DataRecordOrder;

public class DataRecordContainer {
	private DataRecordOrder order = DataRecordOrder.ORDERED;
	private ArrayList<DataRecord> queue = new ArrayList<DataRecord>();
	private String[] headers = null;

	public DataRecordContainer(DataRecordOrder order) {
		this.order = order;
	}

	public DataRecordContainer() {
		this(DataRecordOrder.ORDERED);
	}

	public DataRecordContainer(Object[][] records) {
		this.addAll(records);
	}

	public void setHeaders(String[] names) {
		this.headers = names;
	}

	public void add(DataRecord record) {
		this.queue.add(record);
	}

	public void add(Object[] record) {
		if (this.headers == null) {
			this.queue.add(new DefaultDataRecord(record));
		} else {
			this.queue.add(new DefaultDataRecord(headers, record));
		}
	}

	public void addAll(Object[][] records) {
		if (this.headers == null) {
			for (Object[] record : records) {
				this.queue.add(new DefaultDataRecord(record));
			}
		} else {
			for (Object[] record : records) {
				this.queue.add(new DefaultDataRecord(headers, record));
			}
		}
	}

	public DataRecord get(int index) {
		return this.queue.get(index);
	}

	public ArrayList<DataRecord> getAll() {
		return queue;
	}

	public Iterator<DataRecord> iterator() {
		return queue.iterator();
	}

}
